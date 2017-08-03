""" TUNNEL_MIB 

The MIB module for management of IP Tunnels,
independent of the specific encapsulation scheme in
use.

Copyright (C) The Internet Society (2005).  This
version of this MIB module is part of RFC 4087;  see
the RFC itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TunnelMib(Entity):
    """
    
    
    .. attribute:: tunnelconfigtable
    
    	The (conceptual) table containing information on configured tunnels.  This table can be used to map a set of tunnel endpoints to the associated ifIndex value.  It can also be used for row creation.  Note that every row in the tunnelIfTable with a fixed IPv4 destination address should have a corresponding row in the tunnelConfigTable, regardless of whether it was created via SNMP.  Since this table does not support IPv6, it is deprecated in favor of tunnelInetConfigTable
    	**type**\:   :py:class:`Tunnelconfigtable <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunnelconfigtable>`
    
    	**status**\: deprecated
    
    .. attribute:: tunneliftable
    
    	The (conceptual) table containing information on configured tunnels
    	**type**\:   :py:class:`Tunneliftable <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunneliftable>`
    
    .. attribute:: tunnelinetconfigtable
    
    	The (conceptual) table containing information on configured tunnels.  This table can be used to map a set of tunnel endpoints to the associated ifIndex value.  It can also be used for row creation.  Note that every row in the tunnelIfTable with a fixed destination address should have a corresponding row in the tunnelInetConfigTable, regardless of whether it was created via SNMP
    	**type**\:   :py:class:`Tunnelinetconfigtable <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunnelinetconfigtable>`
    
    

    """

    _prefix = 'TUNNEL-MIB'
    _revision = '2005-05-16'

    def __init__(self):
        super(TunnelMib, self).__init__()
        self._top_entity = None

        self.yang_name = "TUNNEL-MIB"
        self.yang_parent_name = "TUNNEL-MIB"

        self.tunnelconfigtable = TunnelMib.Tunnelconfigtable()
        self.tunnelconfigtable.parent = self
        self._children_name_map["tunnelconfigtable"] = "tunnelConfigTable"
        self._children_yang_names.add("tunnelConfigTable")

        self.tunneliftable = TunnelMib.Tunneliftable()
        self.tunneliftable.parent = self
        self._children_name_map["tunneliftable"] = "tunnelIfTable"
        self._children_yang_names.add("tunnelIfTable")

        self.tunnelinetconfigtable = TunnelMib.Tunnelinetconfigtable()
        self.tunnelinetconfigtable.parent = self
        self._children_name_map["tunnelinetconfigtable"] = "tunnelInetConfigTable"
        self._children_yang_names.add("tunnelInetConfigTable")


    class Tunneliftable(Entity):
        """
        The (conceptual) table containing information on
        configured tunnels.
        
        .. attribute:: tunnelifentry
        
        	An entry (conceptual row) containing the information on a particular configured tunnel
        	**type**\: list of    :py:class:`Tunnelifentry <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunneliftable.Tunnelifentry>`
        
        

        """

        _prefix = 'TUNNEL-MIB'
        _revision = '2005-05-16'

        def __init__(self):
            super(TunnelMib.Tunneliftable, self).__init__()

            self.yang_name = "tunnelIfTable"
            self.yang_parent_name = "TUNNEL-MIB"

            self.tunnelifentry = YList(self)

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
                        super(TunnelMib.Tunneliftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TunnelMib.Tunneliftable, self).__setattr__(name, value)


        class Tunnelifentry(Entity):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: tunnelifaddresstype
            
            	The type of address in the corresponding tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress objects
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: tunnelifencapslimit
            
            	The maximum number of additional encapsulations permitted for packets undergoing encapsulation at this node.  A value of \-1 indicates that no limit is present (except as a result of the packet size)
            	**type**\:  int
            
            	**range:** \-1..255
            
            .. attribute:: tunnelifencapsmethod
            
            	The encapsulation method used by the tunnel
            	**type**\:   :py:class:`Ianatunneltype <ydk.models.cisco_ios_xe.IANAifType_MIB.Ianatunneltype>`
            
            .. attribute:: tunnelifflowlabel
            
            	The method used to set the IPv6 Flow Label value. This object need not be present in rows where tunnelIfAddressType indicates the tunnel is not over IPv6.  A value of \-1 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB.  Any other value indicates that the Flow Label field is set to the indicated value
            	**type**\:  int
            
            	**range:** \-1..100
            
            .. attribute:: tunnelifhoplimit
            
            	The IPv4 TTL or IPv6 Hop Limit to use in the outer IP header.  A value of 0 indicates that the value is copied from the payload's header
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: tunneliflocaladdress
            
            	The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header), or 0.0.0.0 if unknown or if the tunnel is over IPv6.  Since this object does not support IPv6, it is deprecated in favor of tunnelIfLocalInetAddress
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tunneliflocalinetaddress
            
            	The address of the local endpoint of the tunnel (i.e., the source address used in the outer IP header).  If the address is unknown, the value is  0.0.0.0 for IPv4 or \:\: for IPv6.  The type of this object is given by tunnelIfAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tunnelifremoteaddress
            
            	The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header), or 0.0.0.0 if unknown, or an IPv6 address, or  the tunnel is not a point\-to\-point link (e.g., if it is a 6to4 tunnel).  Since this object does not support IPv6, it is deprecated in favor of tunnelIfRemoteInetAddress
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tunnelifremoteinetaddress
            
            	The address of the remote endpoint of the tunnel (i.e., the destination address used in the outer IP header).  If the address is unknown or the tunnel is not a point\-to\-point link (e.g., if it is a 6to4 tunnel), the value is 0.0.0.0 for tunnels over IPv4 or \:\: for tunnels over IPv6.  The type of this object is given by tunnelIfAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tunnelifsecurity
            
            	The method used by the tunnel to secure the outer IP header.  The value ipsec indicates that IPsec is used between the tunnel endpoints for authentication or encryption or both.  More specific security\-related information may be available in a MIB module for the security protocol in use
            	**type**\:   :py:class:`Tunnelifsecurity <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunneliftable.Tunnelifentry.Tunnelifsecurity>`
            
            .. attribute:: tunneliftos
            
            	The method used to set the high 6 bits (the  differentiated services codepoint) of the IPv4 TOS or IPv6 Traffic Class in the outer IP header.  A value of \-1 indicates that the bits are copied from the payload's header.  A value of \-2 indicates that a traffic conditioner is invoked and more information may be available in a traffic conditioner MIB module. A value between 0 and 63 inclusive indicates that the bit field is set to the indicated value.  Note\: instead of the name tunnelIfTOS, a better name would have been tunnelIfDSCPMethod, but the existing name appeared in RFC 2667 and existing objects cannot be renamed
            	**type**\:  int
            
            	**range:** \-2..63
            
            

            """

            _prefix = 'TUNNEL-MIB'
            _revision = '2005-05-16'

            def __init__(self):
                super(TunnelMib.Tunneliftable.Tunnelifentry, self).__init__()

                self.yang_name = "tunnelIfEntry"
                self.yang_parent_name = "tunnelIfTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.tunnelifaddresstype = YLeaf(YType.enumeration, "tunnelIfAddressType")

                self.tunnelifencapslimit = YLeaf(YType.int32, "tunnelIfEncapsLimit")

                self.tunnelifencapsmethod = YLeaf(YType.enumeration, "tunnelIfEncapsMethod")

                self.tunnelifflowlabel = YLeaf(YType.int32, "tunnelIfFlowLabel")

                self.tunnelifhoplimit = YLeaf(YType.int32, "tunnelIfHopLimit")

                self.tunneliflocaladdress = YLeaf(YType.str, "tunnelIfLocalAddress")

                self.tunneliflocalinetaddress = YLeaf(YType.str, "tunnelIfLocalInetAddress")

                self.tunnelifremoteaddress = YLeaf(YType.str, "tunnelIfRemoteAddress")

                self.tunnelifremoteinetaddress = YLeaf(YType.str, "tunnelIfRemoteInetAddress")

                self.tunnelifsecurity = YLeaf(YType.enumeration, "tunnelIfSecurity")

                self.tunneliftos = YLeaf(YType.int32, "tunnelIfTOS")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "tunnelifaddresstype",
                                "tunnelifencapslimit",
                                "tunnelifencapsmethod",
                                "tunnelifflowlabel",
                                "tunnelifhoplimit",
                                "tunneliflocaladdress",
                                "tunneliflocalinetaddress",
                                "tunnelifremoteaddress",
                                "tunnelifremoteinetaddress",
                                "tunnelifsecurity",
                                "tunneliftos") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TunnelMib.Tunneliftable.Tunnelifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TunnelMib.Tunneliftable.Tunnelifentry, self).__setattr__(name, value)

            class Tunnelifsecurity(Enum):
                """
                Tunnelifsecurity

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


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.tunnelifaddresstype.is_set or
                    self.tunnelifencapslimit.is_set or
                    self.tunnelifencapsmethod.is_set or
                    self.tunnelifflowlabel.is_set or
                    self.tunnelifhoplimit.is_set or
                    self.tunneliflocaladdress.is_set or
                    self.tunneliflocalinetaddress.is_set or
                    self.tunnelifremoteaddress.is_set or
                    self.tunnelifremoteinetaddress.is_set or
                    self.tunnelifsecurity.is_set or
                    self.tunneliftos.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.tunnelifaddresstype.yfilter != YFilter.not_set or
                    self.tunnelifencapslimit.yfilter != YFilter.not_set or
                    self.tunnelifencapsmethod.yfilter != YFilter.not_set or
                    self.tunnelifflowlabel.yfilter != YFilter.not_set or
                    self.tunnelifhoplimit.yfilter != YFilter.not_set or
                    self.tunneliflocaladdress.yfilter != YFilter.not_set or
                    self.tunneliflocalinetaddress.yfilter != YFilter.not_set or
                    self.tunnelifremoteaddress.yfilter != YFilter.not_set or
                    self.tunnelifremoteinetaddress.yfilter != YFilter.not_set or
                    self.tunnelifsecurity.yfilter != YFilter.not_set or
                    self.tunneliftos.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tunnelIfEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TUNNEL-MIB:TUNNEL-MIB/tunnelIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.tunnelifaddresstype.is_set or self.tunnelifaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifaddresstype.get_name_leafdata())
                if (self.tunnelifencapslimit.is_set or self.tunnelifencapslimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifencapslimit.get_name_leafdata())
                if (self.tunnelifencapsmethod.is_set or self.tunnelifencapsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifencapsmethod.get_name_leafdata())
                if (self.tunnelifflowlabel.is_set or self.tunnelifflowlabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifflowlabel.get_name_leafdata())
                if (self.tunnelifhoplimit.is_set or self.tunnelifhoplimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifhoplimit.get_name_leafdata())
                if (self.tunneliflocaladdress.is_set or self.tunneliflocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunneliflocaladdress.get_name_leafdata())
                if (self.tunneliflocalinetaddress.is_set or self.tunneliflocalinetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunneliflocalinetaddress.get_name_leafdata())
                if (self.tunnelifremoteaddress.is_set or self.tunnelifremoteaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifremoteaddress.get_name_leafdata())
                if (self.tunnelifremoteinetaddress.is_set or self.tunnelifremoteinetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifremoteinetaddress.get_name_leafdata())
                if (self.tunnelifsecurity.is_set or self.tunnelifsecurity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelifsecurity.get_name_leafdata())
                if (self.tunneliftos.is_set or self.tunneliftos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunneliftos.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "tunnelIfAddressType" or name == "tunnelIfEncapsLimit" or name == "tunnelIfEncapsMethod" or name == "tunnelIfFlowLabel" or name == "tunnelIfHopLimit" or name == "tunnelIfLocalAddress" or name == "tunnelIfLocalInetAddress" or name == "tunnelIfRemoteAddress" or name == "tunnelIfRemoteInetAddress" or name == "tunnelIfSecurity" or name == "tunnelIfTOS"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfAddressType"):
                    self.tunnelifaddresstype = value
                    self.tunnelifaddresstype.value_namespace = name_space
                    self.tunnelifaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfEncapsLimit"):
                    self.tunnelifencapslimit = value
                    self.tunnelifencapslimit.value_namespace = name_space
                    self.tunnelifencapslimit.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfEncapsMethod"):
                    self.tunnelifencapsmethod = value
                    self.tunnelifencapsmethod.value_namespace = name_space
                    self.tunnelifencapsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfFlowLabel"):
                    self.tunnelifflowlabel = value
                    self.tunnelifflowlabel.value_namespace = name_space
                    self.tunnelifflowlabel.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfHopLimit"):
                    self.tunnelifhoplimit = value
                    self.tunnelifhoplimit.value_namespace = name_space
                    self.tunnelifhoplimit.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfLocalAddress"):
                    self.tunneliflocaladdress = value
                    self.tunneliflocaladdress.value_namespace = name_space
                    self.tunneliflocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfLocalInetAddress"):
                    self.tunneliflocalinetaddress = value
                    self.tunneliflocalinetaddress.value_namespace = name_space
                    self.tunneliflocalinetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfRemoteAddress"):
                    self.tunnelifremoteaddress = value
                    self.tunnelifremoteaddress.value_namespace = name_space
                    self.tunnelifremoteaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfRemoteInetAddress"):
                    self.tunnelifremoteinetaddress = value
                    self.tunnelifremoteinetaddress.value_namespace = name_space
                    self.tunnelifremoteinetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfSecurity"):
                    self.tunnelifsecurity = value
                    self.tunnelifsecurity.value_namespace = name_space
                    self.tunnelifsecurity.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelIfTOS"):
                    self.tunneliftos = value
                    self.tunneliftos.value_namespace = name_space
                    self.tunneliftos.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tunnelifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tunnelifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tunnelIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TUNNEL-MIB:TUNNEL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tunnelIfEntry"):
                for c in self.tunnelifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TunnelMib.Tunneliftable.Tunnelifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tunnelifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tunnelIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tunnelconfigtable(Entity):
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
        	**type**\: list of    :py:class:`Tunnelconfigentry <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunnelconfigtable.Tunnelconfigentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'TUNNEL-MIB'
        _revision = '2005-05-16'

        def __init__(self):
            super(TunnelMib.Tunnelconfigtable, self).__init__()

            self.yang_name = "tunnelConfigTable"
            self.yang_parent_name = "TUNNEL-MIB"

            self.tunnelconfigentry = YList(self)

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
                        super(TunnelMib.Tunnelconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TunnelMib.Tunnelconfigtable, self).__setattr__(name, value)


        class Tunnelconfigentry(Entity):
            """
            An entry (conceptual row) containing the information
            on a particular configured tunnel.
            
            Since this entry does not support IPv6, it is
            deprecated in favor of tunnelInetConfigEntry.
            
            .. attribute:: tunnelconfiglocaladdress  <key>
            
            	The address of the local endpoint of the tunnel, or 0.0.0.0 if the device is free to choose any of its addresses at tunnel establishment time.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigLocalAddress
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigremoteaddress  <key>
            
            	The address of the remote endpoint of the tunnel.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigRemoteAddress
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigencapsmethod  <key>
            
            	The encapsulation method used by the tunnel.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigEncapsMethod
            	**type**\:   :py:class:`Ianatunneltype <ydk.models.cisco_ios_xe.IANAifType_MIB.Ianatunneltype>`
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigid  <key>
            
            	An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints.  If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP\-in\-IP), the value of this object is 1.  For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not conflict with an existing row, such as choosing a random number.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigID
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigifindex
            
            	If the value of tunnelConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface.  A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigIfIndex
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: tunnelconfigstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table.  The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active.  To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelConfigID of 1, and set tunnelConfigStatus to createAndGo.  For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo\-random number to use as the tunnelConfigID and set tunnelConfigStatus to createAndGo.  In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo\-random number and retry the operation.  Creating a row in this table will cause an interface index to be assigned by the agent in an implementation\-dependent manner, and corresponding rows will be instantiated in the ifTable and the tunnelIfTable.  The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up.  Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable.  Since this object does not support IPv6, it is deprecated in favor of tunnelInetConfigStatus
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'TUNNEL-MIB'
            _revision = '2005-05-16'

            def __init__(self):
                super(TunnelMib.Tunnelconfigtable.Tunnelconfigentry, self).__init__()

                self.yang_name = "tunnelConfigEntry"
                self.yang_parent_name = "tunnelConfigTable"

                self.tunnelconfiglocaladdress = YLeaf(YType.str, "tunnelConfigLocalAddress")

                self.tunnelconfigremoteaddress = YLeaf(YType.str, "tunnelConfigRemoteAddress")

                self.tunnelconfigencapsmethod = YLeaf(YType.enumeration, "tunnelConfigEncapsMethod")

                self.tunnelconfigid = YLeaf(YType.int32, "tunnelConfigID")

                self.tunnelconfigifindex = YLeaf(YType.int32, "tunnelConfigIfIndex")

                self.tunnelconfigstatus = YLeaf(YType.enumeration, "tunnelConfigStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tunnelconfiglocaladdress",
                                "tunnelconfigremoteaddress",
                                "tunnelconfigencapsmethod",
                                "tunnelconfigid",
                                "tunnelconfigifindex",
                                "tunnelconfigstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TunnelMib.Tunnelconfigtable.Tunnelconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TunnelMib.Tunnelconfigtable.Tunnelconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tunnelconfiglocaladdress.is_set or
                    self.tunnelconfigremoteaddress.is_set or
                    self.tunnelconfigencapsmethod.is_set or
                    self.tunnelconfigid.is_set or
                    self.tunnelconfigifindex.is_set or
                    self.tunnelconfigstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tunnelconfiglocaladdress.yfilter != YFilter.not_set or
                    self.tunnelconfigremoteaddress.yfilter != YFilter.not_set or
                    self.tunnelconfigencapsmethod.yfilter != YFilter.not_set or
                    self.tunnelconfigid.yfilter != YFilter.not_set or
                    self.tunnelconfigifindex.yfilter != YFilter.not_set or
                    self.tunnelconfigstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tunnelConfigEntry" + "[tunnelConfigLocalAddress='" + self.tunnelconfiglocaladdress.get() + "']" + "[tunnelConfigRemoteAddress='" + self.tunnelconfigremoteaddress.get() + "']" + "[tunnelConfigEncapsMethod='" + self.tunnelconfigencapsmethod.get() + "']" + "[tunnelConfigID='" + self.tunnelconfigid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TUNNEL-MIB:TUNNEL-MIB/tunnelConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tunnelconfiglocaladdress.is_set or self.tunnelconfiglocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelconfiglocaladdress.get_name_leafdata())
                if (self.tunnelconfigremoteaddress.is_set or self.tunnelconfigremoteaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelconfigremoteaddress.get_name_leafdata())
                if (self.tunnelconfigencapsmethod.is_set or self.tunnelconfigencapsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelconfigencapsmethod.get_name_leafdata())
                if (self.tunnelconfigid.is_set or self.tunnelconfigid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelconfigid.get_name_leafdata())
                if (self.tunnelconfigifindex.is_set or self.tunnelconfigifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelconfigifindex.get_name_leafdata())
                if (self.tunnelconfigstatus.is_set or self.tunnelconfigstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelconfigstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tunnelConfigLocalAddress" or name == "tunnelConfigRemoteAddress" or name == "tunnelConfigEncapsMethod" or name == "tunnelConfigID" or name == "tunnelConfigIfIndex" or name == "tunnelConfigStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tunnelConfigLocalAddress"):
                    self.tunnelconfiglocaladdress = value
                    self.tunnelconfiglocaladdress.value_namespace = name_space
                    self.tunnelconfiglocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelConfigRemoteAddress"):
                    self.tunnelconfigremoteaddress = value
                    self.tunnelconfigremoteaddress.value_namespace = name_space
                    self.tunnelconfigremoteaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelConfigEncapsMethod"):
                    self.tunnelconfigencapsmethod = value
                    self.tunnelconfigencapsmethod.value_namespace = name_space
                    self.tunnelconfigencapsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelConfigID"):
                    self.tunnelconfigid = value
                    self.tunnelconfigid.value_namespace = name_space
                    self.tunnelconfigid.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelConfigIfIndex"):
                    self.tunnelconfigifindex = value
                    self.tunnelconfigifindex.value_namespace = name_space
                    self.tunnelconfigifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelConfigStatus"):
                    self.tunnelconfigstatus = value
                    self.tunnelconfigstatus.value_namespace = name_space
                    self.tunnelconfigstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tunnelconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tunnelconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tunnelConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TUNNEL-MIB:TUNNEL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tunnelConfigEntry"):
                for c in self.tunnelconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TunnelMib.Tunnelconfigtable.Tunnelconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tunnelconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tunnelConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tunnelinetconfigtable(Entity):
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
        	**type**\: list of    :py:class:`Tunnelinetconfigentry <ydk.models.cisco_ios_xe.TUNNEL_MIB.TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry>`
        
        

        """

        _prefix = 'TUNNEL-MIB'
        _revision = '2005-05-16'

        def __init__(self):
            super(TunnelMib.Tunnelinetconfigtable, self).__init__()

            self.yang_name = "tunnelInetConfigTable"
            self.yang_parent_name = "TUNNEL-MIB"

            self.tunnelinetconfigentry = YList(self)

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
                        super(TunnelMib.Tunnelinetconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(TunnelMib.Tunnelinetconfigtable, self).__setattr__(name, value)


        class Tunnelinetconfigentry(Entity):
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
            
            .. attribute:: tunnelinetconfigaddresstype  <key>
            
            	The address type over which the tunnel encapsulates packets
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: tunnelinetconfiglocaladdress  <key>
            
            	The address of the local endpoint of the tunnel, or 0.0.0.0 (for IPv4) or \:\: (for IPv6) if the device is free to choose any of its addresses at tunnel establishment time
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tunnelinetconfigremoteaddress  <key>
            
            	The address of the remote endpoint of the tunnel
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: tunnelinetconfigencapsmethod  <key>
            
            	The encapsulation method used by the tunnel
            	**type**\:   :py:class:`Ianatunneltype <ydk.models.cisco_ios_xe.IANAifType_MIB.Ianatunneltype>`
            
            .. attribute:: tunnelinetconfigid  <key>
            
            	An identifier used to distinguish between multiple tunnels of the same encapsulation method, with the same endpoints.  If the encapsulation protocol only allows one tunnel per set of endpoint addresses (such as for GRE or IP\-in\-IP), the value of this object is 1.  For encapsulation methods (such as L2F) which allow multiple parallel tunnels, the manager is responsible for choosing any ID which does not  conflict with an existing row, such as choosing a random number
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: tunnelinetconfigifindex
            
            	If the value of tunnelInetConfigStatus for this row is active, then this object contains the value of ifIndex corresponding to the tunnel interface.  A value of 0 is not legal in the active state, and means that the interface index has not yet been assigned
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: tunnelinetconfigstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table.  The agent need not support setting this object to createAndWait or notInService since there are no other writable objects in this table, and writable objects in rows of corresponding tables such as the tunnelIfTable may be modified while this row is active.  To create a row in this table for an encapsulation method which does not support multiple parallel tunnels with the same endpoints, the management station should simply use a tunnelInetConfigID of 1, and set tunnelInetConfigStatus to createAndGo.  For encapsulation methods such as L2F which allow multiple parallel tunnels, the management station may select a pseudo\-random number to use as the tunnelInetConfigID and set tunnelInetConfigStatus to createAndGo.  In the event that this ID is already in use and an inconsistentValue is returned in response to the set operation, the management station should simply select a new pseudo\-random number and retry the operation.  Creating a row in this table will cause an interface index to be assigned by the agent in an implementation\-dependent manner, and corresponding rows will be instantiated in the ifTable and the  tunnelIfTable.  The status of this row will become active as soon as the agent assigns the interface index, regardless of whether the interface is operationally up.  Deleting a row in this table will likewise delete the corresponding row in the ifTable and in the tunnelIfTable
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: tunnelinetconfigstoragetype
            
            	The storage type of this row.  If the row is permanent(4), no objects in the row need be writable
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'TUNNEL-MIB'
            _revision = '2005-05-16'

            def __init__(self):
                super(TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry, self).__init__()

                self.yang_name = "tunnelInetConfigEntry"
                self.yang_parent_name = "tunnelInetConfigTable"

                self.tunnelinetconfigaddresstype = YLeaf(YType.enumeration, "tunnelInetConfigAddressType")

                self.tunnelinetconfiglocaladdress = YLeaf(YType.str, "tunnelInetConfigLocalAddress")

                self.tunnelinetconfigremoteaddress = YLeaf(YType.str, "tunnelInetConfigRemoteAddress")

                self.tunnelinetconfigencapsmethod = YLeaf(YType.enumeration, "tunnelInetConfigEncapsMethod")

                self.tunnelinetconfigid = YLeaf(YType.int32, "tunnelInetConfigID")

                self.tunnelinetconfigifindex = YLeaf(YType.int32, "tunnelInetConfigIfIndex")

                self.tunnelinetconfigstatus = YLeaf(YType.enumeration, "tunnelInetConfigStatus")

                self.tunnelinetconfigstoragetype = YLeaf(YType.enumeration, "tunnelInetConfigStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("tunnelinetconfigaddresstype",
                                "tunnelinetconfiglocaladdress",
                                "tunnelinetconfigremoteaddress",
                                "tunnelinetconfigencapsmethod",
                                "tunnelinetconfigid",
                                "tunnelinetconfigifindex",
                                "tunnelinetconfigstatus",
                                "tunnelinetconfigstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.tunnelinetconfigaddresstype.is_set or
                    self.tunnelinetconfiglocaladdress.is_set or
                    self.tunnelinetconfigremoteaddress.is_set or
                    self.tunnelinetconfigencapsmethod.is_set or
                    self.tunnelinetconfigid.is_set or
                    self.tunnelinetconfigifindex.is_set or
                    self.tunnelinetconfigstatus.is_set or
                    self.tunnelinetconfigstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.tunnelinetconfigaddresstype.yfilter != YFilter.not_set or
                    self.tunnelinetconfiglocaladdress.yfilter != YFilter.not_set or
                    self.tunnelinetconfigremoteaddress.yfilter != YFilter.not_set or
                    self.tunnelinetconfigencapsmethod.yfilter != YFilter.not_set or
                    self.tunnelinetconfigid.yfilter != YFilter.not_set or
                    self.tunnelinetconfigifindex.yfilter != YFilter.not_set or
                    self.tunnelinetconfigstatus.yfilter != YFilter.not_set or
                    self.tunnelinetconfigstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tunnelInetConfigEntry" + "[tunnelInetConfigAddressType='" + self.tunnelinetconfigaddresstype.get() + "']" + "[tunnelInetConfigLocalAddress='" + self.tunnelinetconfiglocaladdress.get() + "']" + "[tunnelInetConfigRemoteAddress='" + self.tunnelinetconfigremoteaddress.get() + "']" + "[tunnelInetConfigEncapsMethod='" + self.tunnelinetconfigencapsmethod.get() + "']" + "[tunnelInetConfigID='" + self.tunnelinetconfigid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "TUNNEL-MIB:TUNNEL-MIB/tunnelInetConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.tunnelinetconfigaddresstype.is_set or self.tunnelinetconfigaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigaddresstype.get_name_leafdata())
                if (self.tunnelinetconfiglocaladdress.is_set or self.tunnelinetconfiglocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfiglocaladdress.get_name_leafdata())
                if (self.tunnelinetconfigremoteaddress.is_set or self.tunnelinetconfigremoteaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigremoteaddress.get_name_leafdata())
                if (self.tunnelinetconfigencapsmethod.is_set or self.tunnelinetconfigencapsmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigencapsmethod.get_name_leafdata())
                if (self.tunnelinetconfigid.is_set or self.tunnelinetconfigid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigid.get_name_leafdata())
                if (self.tunnelinetconfigifindex.is_set or self.tunnelinetconfigifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigifindex.get_name_leafdata())
                if (self.tunnelinetconfigstatus.is_set or self.tunnelinetconfigstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigstatus.get_name_leafdata())
                if (self.tunnelinetconfigstoragetype.is_set or self.tunnelinetconfigstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnelinetconfigstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "tunnelInetConfigAddressType" or name == "tunnelInetConfigLocalAddress" or name == "tunnelInetConfigRemoteAddress" or name == "tunnelInetConfigEncapsMethod" or name == "tunnelInetConfigID" or name == "tunnelInetConfigIfIndex" or name == "tunnelInetConfigStatus" or name == "tunnelInetConfigStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "tunnelInetConfigAddressType"):
                    self.tunnelinetconfigaddresstype = value
                    self.tunnelinetconfigaddresstype.value_namespace = name_space
                    self.tunnelinetconfigaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigLocalAddress"):
                    self.tunnelinetconfiglocaladdress = value
                    self.tunnelinetconfiglocaladdress.value_namespace = name_space
                    self.tunnelinetconfiglocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigRemoteAddress"):
                    self.tunnelinetconfigremoteaddress = value
                    self.tunnelinetconfigremoteaddress.value_namespace = name_space
                    self.tunnelinetconfigremoteaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigEncapsMethod"):
                    self.tunnelinetconfigencapsmethod = value
                    self.tunnelinetconfigencapsmethod.value_namespace = name_space
                    self.tunnelinetconfigencapsmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigID"):
                    self.tunnelinetconfigid = value
                    self.tunnelinetconfigid.value_namespace = name_space
                    self.tunnelinetconfigid.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigIfIndex"):
                    self.tunnelinetconfigifindex = value
                    self.tunnelinetconfigifindex.value_namespace = name_space
                    self.tunnelinetconfigifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigStatus"):
                    self.tunnelinetconfigstatus = value
                    self.tunnelinetconfigstatus.value_namespace = name_space
                    self.tunnelinetconfigstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnelInetConfigStorageType"):
                    self.tunnelinetconfigstoragetype = value
                    self.tunnelinetconfigstoragetype.value_namespace = name_space
                    self.tunnelinetconfigstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tunnelinetconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tunnelinetconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tunnelInetConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "TUNNEL-MIB:TUNNEL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tunnelInetConfigEntry"):
                for c in self.tunnelinetconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = TunnelMib.Tunnelinetconfigtable.Tunnelinetconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tunnelinetconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tunnelInetConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.tunnelconfigtable is not None and self.tunnelconfigtable.has_data()) or
            (self.tunneliftable is not None and self.tunneliftable.has_data()) or
            (self.tunnelinetconfigtable is not None and self.tunnelinetconfigtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.tunnelconfigtable is not None and self.tunnelconfigtable.has_operation()) or
            (self.tunneliftable is not None and self.tunneliftable.has_operation()) or
            (self.tunnelinetconfigtable is not None and self.tunnelinetconfigtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "TUNNEL-MIB:TUNNEL-MIB" + path_buffer

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

        if (child_yang_name == "tunnelConfigTable"):
            if (self.tunnelconfigtable is None):
                self.tunnelconfigtable = TunnelMib.Tunnelconfigtable()
                self.tunnelconfigtable.parent = self
                self._children_name_map["tunnelconfigtable"] = "tunnelConfigTable"
            return self.tunnelconfigtable

        if (child_yang_name == "tunnelIfTable"):
            if (self.tunneliftable is None):
                self.tunneliftable = TunnelMib.Tunneliftable()
                self.tunneliftable.parent = self
                self._children_name_map["tunneliftable"] = "tunnelIfTable"
            return self.tunneliftable

        if (child_yang_name == "tunnelInetConfigTable"):
            if (self.tunnelinetconfigtable is None):
                self.tunnelinetconfigtable = TunnelMib.Tunnelinetconfigtable()
                self.tunnelinetconfigtable.parent = self
                self._children_name_map["tunnelinetconfigtable"] = "tunnelInetConfigTable"
            return self.tunnelinetconfigtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "tunnelConfigTable" or name == "tunnelIfTable" or name == "tunnelInetConfigTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = TunnelMib()
        return self._top_entity


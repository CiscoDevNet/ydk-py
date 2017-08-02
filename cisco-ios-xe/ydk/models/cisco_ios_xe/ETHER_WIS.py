""" ETHER_WIS 

The objects in this MIB module are used in conjunction
with objects in the SONET\-MIB and the MAU\-MIB to manage
the Ethernet WAN Interface Sublayer (WIS).

The following reference is used throughout this MIB module\:

[IEEE 802.3 Std] refers to\:
   IEEE Std 802.3, 2000 Edition\: 'IEEE Standard for
   Information technology \- Telecommunications and
   information exchange between systems \- Local and
   metropolitan area networks \- Specific requirements \-
   Part 3\: Carrier sense multiple access with collision
   detection (CSMA/CD) access method and physical layer
   specifications', as amended by IEEE Std 802.3ae\-2002,
   'IEEE Standard for Carrier Sense Multiple Access with
   Collision Detection (CSMA/CD) Access Method and
   Physical Layer Specifications \- Media Access Control
   (MAC) Parameters, Physical Layer and Management
   Parameters for 10 Gb/s Operation', 30 August 2002.

Of particular interest are Clause 50, 'WAN Interface
Sublayer (WIS), type 10GBASE\-W', Clause 30, '10Mb/s,
100Mb/s, 1000Mb/s, and 10Gb/s MAC Control, and Link
Aggregation Management', and Clause 45, 'Management
Data Input/Output (MDIO) Interface'.

Copyright (C) The Internet Society (2003).  This version
of this MIB module is part of RFC 3637;  see the RFC
itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EtherWis(Entity):
    """
    
    
    .. attribute:: etherwisdevicetable
    
    	The table for Ethernet WIS devices
    	**type**\:   :py:class:`Etherwisdevicetable <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisdevicetable>`
    
    .. attribute:: etherwisfarendpathcurrenttable
    
    	The table for the current far\-end state of Ethernet WIS paths
    	**type**\:   :py:class:`Etherwisfarendpathcurrenttable <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisfarendpathcurrenttable>`
    
    .. attribute:: etherwispathcurrenttable
    
    	The table for the current state of Ethernet WIS paths
    	**type**\:   :py:class:`Etherwispathcurrenttable <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwispathcurrenttable>`
    
    .. attribute:: etherwissectioncurrenttable
    
    	The table for the current state of Ethernet WIS sections
    	**type**\:   :py:class:`Etherwissectioncurrenttable <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwissectioncurrenttable>`
    
    

    """

    _prefix = 'ETHER-WIS'
    _revision = '2003-09-19'

    def __init__(self):
        super(EtherWis, self).__init__()
        self._top_entity = None

        self.yang_name = "ETHER-WIS"
        self.yang_parent_name = "ETHER-WIS"

        self.etherwisdevicetable = EtherWis.Etherwisdevicetable()
        self.etherwisdevicetable.parent = self
        self._children_name_map["etherwisdevicetable"] = "etherWisDeviceTable"
        self._children_yang_names.add("etherWisDeviceTable")

        self.etherwisfarendpathcurrenttable = EtherWis.Etherwisfarendpathcurrenttable()
        self.etherwisfarendpathcurrenttable.parent = self
        self._children_name_map["etherwisfarendpathcurrenttable"] = "etherWisFarEndPathCurrentTable"
        self._children_yang_names.add("etherWisFarEndPathCurrentTable")

        self.etherwispathcurrenttable = EtherWis.Etherwispathcurrenttable()
        self.etherwispathcurrenttable.parent = self
        self._children_name_map["etherwispathcurrenttable"] = "etherWisPathCurrentTable"
        self._children_yang_names.add("etherWisPathCurrentTable")

        self.etherwissectioncurrenttable = EtherWis.Etherwissectioncurrenttable()
        self.etherwissectioncurrenttable.parent = self
        self._children_name_map["etherwissectioncurrenttable"] = "etherWisSectionCurrentTable"
        self._children_yang_names.add("etherWisSectionCurrentTable")


    class Etherwisdevicetable(Entity):
        """
        The table for Ethernet WIS devices
        
        .. attribute:: etherwisdeviceentry
        
        	An entry in the Ethernet WIS device table.  For each instance of this object there MUST be a corresponding instance of sonetMediumEntry
        	**type**\: list of    :py:class:`Etherwisdeviceentry <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisdevicetable.Etherwisdeviceentry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherWis.Etherwisdevicetable, self).__init__()

            self.yang_name = "etherWisDeviceTable"
            self.yang_parent_name = "ETHER-WIS"

            self.etherwisdeviceentry = YList(self)

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
                        super(EtherWis.Etherwisdevicetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherWis.Etherwisdevicetable, self).__setattr__(name, value)


        class Etherwisdeviceentry(Entity):
            """
            An entry in the Ethernet WIS device table.  For each
            instance of this object there MUST be a corresponding
            instance of sonetMediumEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: etherwisdevicerxtestpatternerrors
            
            	This object counts the number of errors detected when the WIS receive path is operating in the PRBS31 test pattern mode.  It is reset to zero when the WIS receive path initially enters that mode, and it increments each time the PRBS pattern checker detects an error as described in [IEEE 802.3 Std.] subclause 50.3.8.2 unless its value is 65535, in which case it remains unchanged.  This object is writeable so that it may be reset upon explicit request of a command generator application while the WIS receive path continues to operate in PRBS31 test pattern mode
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: etherwisdevicerxtestpatternmode
            
            	This variable controls the receive test pattern mode. The value none(1) puts the the WIS receive path into the normal operating mode.  The value prbs31(3) puts the WIS receive path into the PRBS31 test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value mixedFrequency(4) puts the WIS receive path into the mixed frequency test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.3.  Any attempt to set this object to a value other than none(1) when the corresponding instance of ifAdminStatus has the value up(1) MUST be rejected with the error inconsistentValue, and any attempt to set the corresponding instance of ifAdminStatus to the value up(1) when an instance of this object has a value other than none(1) MUST be rejected with the error inconsistentValue
            	**type**\:   :py:class:`Etherwisdevicerxtestpatternmode <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisdevicetable.Etherwisdeviceentry.Etherwisdevicerxtestpatternmode>`
            
            .. attribute:: etherwisdevicetxtestpatternmode
            
            	This variable controls the transmit test pattern mode. The value none(1) puts the the WIS transmit path into the normal operating mode.  The value squareWave(2) puts the WIS transmit path into the square wave test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.1. The value prbs31(3) puts the WIS transmit path into the PRBS31 test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value mixedFrequency(4) puts the WIS transmit path into the mixed frequency test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.3. Any attempt to set this object to a value other than none(1) when the corresponding instance of ifAdminStatus has the value up(1) MUST be rejected with the error inconsistentValue, and any attempt to set the corresponding instance of ifAdminStatus to the value up(1) when an instance of this object has a value other than none(1) MUST be rejected with the error inconsistentValue
            	**type**\:   :py:class:`Etherwisdevicetxtestpatternmode <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisdevicetable.Etherwisdeviceentry.Etherwisdevicetxtestpatternmode>`
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherWis.Etherwisdevicetable.Etherwisdeviceentry, self).__init__()

                self.yang_name = "etherWisDeviceEntry"
                self.yang_parent_name = "etherWisDeviceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.etherwisdevicerxtestpatternerrors = YLeaf(YType.uint32, "etherWisDeviceRxTestPatternErrors")

                self.etherwisdevicerxtestpatternmode = YLeaf(YType.enumeration, "etherWisDeviceRxTestPatternMode")

                self.etherwisdevicetxtestpatternmode = YLeaf(YType.enumeration, "etherWisDeviceTxTestPatternMode")

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
                                "etherwisdevicerxtestpatternerrors",
                                "etherwisdevicerxtestpatternmode",
                                "etherwisdevicetxtestpatternmode") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherWis.Etherwisdevicetable.Etherwisdeviceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherWis.Etherwisdevicetable.Etherwisdeviceentry, self).__setattr__(name, value)

            class Etherwisdevicerxtestpatternmode(Enum):
                """
                Etherwisdevicerxtestpatternmode

                This variable controls the receive test pattern mode.

                The value none(1) puts the the WIS receive path into the

                normal operating mode.  The value prbs31(3) puts the WIS

                receive path into the PRBS31 test pattern mode described

                in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value

                mixedFrequency(4) puts the WIS receive path into the mixed

                frequency test pattern mode described in [IEEE 802.3 Std.]

                subclause 50.3.8.3.  Any attempt to set this object to a

                value other than none(1) when the corresponding instance

                of ifAdminStatus has the value up(1) MUST be rejected with

                the error inconsistentValue, and any attempt to set the

                corresponding instance of ifAdminStatus to the value up(1)

                when an instance of this object has a value other than

                none(1) MUST be rejected with the error inconsistentValue.

                .. data:: none = 1

                .. data:: prbs31 = 3

                .. data:: mixedFrequency = 4

                """

                none = Enum.YLeaf(1, "none")

                prbs31 = Enum.YLeaf(3, "prbs31")

                mixedFrequency = Enum.YLeaf(4, "mixedFrequency")


            class Etherwisdevicetxtestpatternmode(Enum):
                """
                Etherwisdevicetxtestpatternmode

                This variable controls the transmit test pattern mode.

                The value none(1) puts the the WIS transmit path into

                the normal operating mode.  The value squareWave(2) puts

                the WIS transmit path into the square wave test pattern

                mode described in [IEEE 802.3 Std.] subclause 50.3.8.1.

                The value prbs31(3) puts the WIS transmit path into the

                PRBS31 test pattern mode described in [IEEE 802.3 Std.]

                subclause 50.3.8.2.  The value mixedFrequency(4) puts the

                WIS transmit path into the mixed frequency test pattern

                mode described in [IEEE 802.3 Std.] subclause 50.3.8.3.

                Any attempt to set this object to a value other than

                none(1) when the corresponding instance of ifAdminStatus

                has the value up(1) MUST be rejected with the error

                inconsistentValue, and any attempt to set the corresponding

                instance of ifAdminStatus to the value up(1) when an

                instance of this object has a value other than none(1)

                MUST be rejected with the error inconsistentValue.

                .. data:: none = 1

                .. data:: squareWave = 2

                .. data:: prbs31 = 3

                .. data:: mixedFrequency = 4

                """

                none = Enum.YLeaf(1, "none")

                squareWave = Enum.YLeaf(2, "squareWave")

                prbs31 = Enum.YLeaf(3, "prbs31")

                mixedFrequency = Enum.YLeaf(4, "mixedFrequency")


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.etherwisdevicerxtestpatternerrors.is_set or
                    self.etherwisdevicerxtestpatternmode.is_set or
                    self.etherwisdevicetxtestpatternmode.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.etherwisdevicerxtestpatternerrors.yfilter != YFilter.not_set or
                    self.etherwisdevicerxtestpatternmode.yfilter != YFilter.not_set or
                    self.etherwisdevicetxtestpatternmode.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etherWisDeviceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ETHER-WIS:ETHER-WIS/etherWisDeviceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.etherwisdevicerxtestpatternerrors.is_set or self.etherwisdevicerxtestpatternerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwisdevicerxtestpatternerrors.get_name_leafdata())
                if (self.etherwisdevicerxtestpatternmode.is_set or self.etherwisdevicerxtestpatternmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwisdevicerxtestpatternmode.get_name_leafdata())
                if (self.etherwisdevicetxtestpatternmode.is_set or self.etherwisdevicetxtestpatternmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwisdevicetxtestpatternmode.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "etherWisDeviceRxTestPatternErrors" or name == "etherWisDeviceRxTestPatternMode" or name == "etherWisDeviceTxTestPatternMode"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisDeviceRxTestPatternErrors"):
                    self.etherwisdevicerxtestpatternerrors = value
                    self.etherwisdevicerxtestpatternerrors.value_namespace = name_space
                    self.etherwisdevicerxtestpatternerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisDeviceRxTestPatternMode"):
                    self.etherwisdevicerxtestpatternmode = value
                    self.etherwisdevicerxtestpatternmode.value_namespace = name_space
                    self.etherwisdevicerxtestpatternmode.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisDeviceTxTestPatternMode"):
                    self.etherwisdevicetxtestpatternmode = value
                    self.etherwisdevicetxtestpatternmode.value_namespace = name_space
                    self.etherwisdevicetxtestpatternmode.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.etherwisdeviceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.etherwisdeviceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "etherWisDeviceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ETHER-WIS:ETHER-WIS/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "etherWisDeviceEntry"):
                for c in self.etherwisdeviceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherWis.Etherwisdevicetable.Etherwisdeviceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.etherwisdeviceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "etherWisDeviceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Etherwissectioncurrenttable(Entity):
        """
        The table for the current state of Ethernet WIS sections.
        
        .. attribute:: etherwissectioncurrententry
        
        	An entry in the etherWisSectionCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetSectionCurrentEntry
        	**type**\: list of    :py:class:`Etherwissectioncurrententry <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherWis.Etherwissectioncurrenttable, self).__init__()

            self.yang_name = "etherWisSectionCurrentTable"
            self.yang_parent_name = "ETHER-WIS"

            self.etherwissectioncurrententry = YList(self)

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
                        super(EtherWis.Etherwissectioncurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherWis.Etherwissectioncurrenttable, self).__setattr__(name, value)


        class Etherwissectioncurrententry(Entity):
            """
            An entry in the etherWisSectionCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetSectionCurrentEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: etherwissectioncurrentj0received
            
            	This is the 16\-octet section trace message that was most recently received in the J0 byte
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: etherwissectioncurrentj0transmitted
            
            	This is the 16\-octet section trace message that is transmitted in the J0 byte.  The value SHOULD be '89'h followed by fifteen octets of '00'h (or some cyclic shift thereof) when the section trace function is not used, and the implementation SHOULD use that value (or a cyclic shift thereof) as a default if no other value has been set
            	**type**\:  str
            
            	**length:** 16
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry, self).__init__()

                self.yang_name = "etherWisSectionCurrentEntry"
                self.yang_parent_name = "etherWisSectionCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.etherwissectioncurrentj0received = YLeaf(YType.str, "etherWisSectionCurrentJ0Received")

                self.etherwissectioncurrentj0transmitted = YLeaf(YType.str, "etherWisSectionCurrentJ0Transmitted")

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
                                "etherwissectioncurrentj0received",
                                "etherwissectioncurrentj0transmitted") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.etherwissectioncurrentj0received.is_set or
                    self.etherwissectioncurrentj0transmitted.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.etherwissectioncurrentj0received.yfilter != YFilter.not_set or
                    self.etherwissectioncurrentj0transmitted.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etherWisSectionCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ETHER-WIS:ETHER-WIS/etherWisSectionCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.etherwissectioncurrentj0received.is_set or self.etherwissectioncurrentj0received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwissectioncurrentj0received.get_name_leafdata())
                if (self.etherwissectioncurrentj0transmitted.is_set or self.etherwissectioncurrentj0transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwissectioncurrentj0transmitted.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "etherWisSectionCurrentJ0Received" or name == "etherWisSectionCurrentJ0Transmitted"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisSectionCurrentJ0Received"):
                    self.etherwissectioncurrentj0received = value
                    self.etherwissectioncurrentj0received.value_namespace = name_space
                    self.etherwissectioncurrentj0received.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisSectionCurrentJ0Transmitted"):
                    self.etherwissectioncurrentj0transmitted = value
                    self.etherwissectioncurrentj0transmitted.value_namespace = name_space
                    self.etherwissectioncurrentj0transmitted.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.etherwissectioncurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.etherwissectioncurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "etherWisSectionCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ETHER-WIS:ETHER-WIS/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "etherWisSectionCurrentEntry"):
                for c in self.etherwissectioncurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.etherwissectioncurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "etherWisSectionCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Etherwispathcurrenttable(Entity):
        """
        The table for the current state of Ethernet WIS paths.
        
        .. attribute:: etherwispathcurrententry
        
        	An entry in the etherWisPathCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetPathCurrentEntry
        	**type**\: list of    :py:class:`Etherwispathcurrententry <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherWis.Etherwispathcurrenttable, self).__init__()

            self.yang_name = "etherWisPathCurrentTable"
            self.yang_parent_name = "ETHER-WIS"

            self.etherwispathcurrententry = YList(self)

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
                        super(EtherWis.Etherwispathcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherWis.Etherwispathcurrenttable, self).__setattr__(name, value)


        class Etherwispathcurrententry(Entity):
            """
            An entry in the etherWisPathCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetPathCurrentEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: etherwispathcurrentj1received
            
            	This is the 16\-octet path trace message that was most recently received in the J1 byte
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: etherwispathcurrentj1transmitted
            
            	This is the 16\-octet path trace message that is transmitted in the J1 byte.  The value SHOULD be '89'h followed by fifteen octets of '00'h (or some cyclic shift thereof) when the path trace function is not used, and the implementation SHOULD use that value (or a cyclic shift thereof) as a default if no other value has been set
            	**type**\:  str
            
            	**length:** 16
            
            .. attribute:: etherwispathcurrentstatus
            
            	This variable indicates the current status of the path payload with a bit map that can indicate multiple defects at once.  The bit positions are assigned as follows\:  etherWisPathLOP(0)    This bit is set to indicate that an    LOP\-P (Loss of Pointer \- Path) defect    is being experienced.  Note\:  when this    bit is set, sonetPathSTSLOP MUST be set    in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathAIS(1)    This bit is set to indicate that an    AIS\-P (Alarm Indication Signal \- Path)    defect is being experienced.  Note\:  when    this bit is set, sonetPathSTSAIS MUST be    set in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathPLM(1)    This bit is set to indicate that a    PLM\-P (Payload Label Mismatch \- Path)    defect is being experienced.  Note\:  when    this bit is set, sonetPathSignalLabelMismatch    MUST be set in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathLCD(3)    This bit is set to indicate that an    LCD\-P (Loss of Codegroup Delination \- Path)    defect is being experienced.  Since this    defect is detected by the PCS and not by    the path layer itself, there is no    corresponding bit in sonetPathCurrentStatus
            	**type**\:   :py:class:`Etherwispathcurrentstatus <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry.Etherwispathcurrentstatus>`
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry, self).__init__()

                self.yang_name = "etherWisPathCurrentEntry"
                self.yang_parent_name = "etherWisPathCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.etherwispathcurrentj1received = YLeaf(YType.str, "etherWisPathCurrentJ1Received")

                self.etherwispathcurrentj1transmitted = YLeaf(YType.str, "etherWisPathCurrentJ1Transmitted")

                self.etherwispathcurrentstatus = YLeaf(YType.bits, "etherWisPathCurrentStatus")

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
                                "etherwispathcurrentj1received",
                                "etherwispathcurrentj1transmitted",
                                "etherwispathcurrentstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.etherwispathcurrentj1received.is_set or
                    self.etherwispathcurrentj1transmitted.is_set or
                    self.etherwispathcurrentstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.etherwispathcurrentj1received.yfilter != YFilter.not_set or
                    self.etherwispathcurrentj1transmitted.yfilter != YFilter.not_set or
                    self.etherwispathcurrentstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etherWisPathCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ETHER-WIS:ETHER-WIS/etherWisPathCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.etherwispathcurrentj1received.is_set or self.etherwispathcurrentj1received.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwispathcurrentj1received.get_name_leafdata())
                if (self.etherwispathcurrentj1transmitted.is_set or self.etherwispathcurrentj1transmitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwispathcurrentj1transmitted.get_name_leafdata())
                if (self.etherwispathcurrentstatus.is_set or self.etherwispathcurrentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwispathcurrentstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "etherWisPathCurrentJ1Received" or name == "etherWisPathCurrentJ1Transmitted" or name == "etherWisPathCurrentStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisPathCurrentJ1Received"):
                    self.etherwispathcurrentj1received = value
                    self.etherwispathcurrentj1received.value_namespace = name_space
                    self.etherwispathcurrentj1received.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisPathCurrentJ1Transmitted"):
                    self.etherwispathcurrentj1transmitted = value
                    self.etherwispathcurrentj1transmitted.value_namespace = name_space
                    self.etherwispathcurrentj1transmitted.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisPathCurrentStatus"):
                    self.etherwispathcurrentstatus[value] = True

        def has_data(self):
            for c in self.etherwispathcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.etherwispathcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "etherWisPathCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ETHER-WIS:ETHER-WIS/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "etherWisPathCurrentEntry"):
                for c in self.etherwispathcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.etherwispathcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "etherWisPathCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Etherwisfarendpathcurrenttable(Entity):
        """
        The table for the current far\-end state of Ethernet WIS
        paths.
        
        .. attribute:: etherwisfarendpathcurrententry
        
        	An entry in the etherWisFarEndPathCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetFarEndPathCurrentEntry
        	**type**\: list of    :py:class:`Etherwisfarendpathcurrententry <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(EtherWis.Etherwisfarendpathcurrenttable, self).__init__()

            self.yang_name = "etherWisFarEndPathCurrentTable"
            self.yang_parent_name = "ETHER-WIS"

            self.etherwisfarendpathcurrententry = YList(self)

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
                        super(EtherWis.Etherwisfarendpathcurrenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EtherWis.Etherwisfarendpathcurrenttable, self).__setattr__(name, value)


        class Etherwisfarendpathcurrententry(Entity):
            """
            An entry in the etherWisFarEndPathCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetFarEndPathCurrentEntry.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: etherwisfarendpathcurrentstatus
            
            	This variable indicates the current status at the far end of the path using a bit map that can indicate multiple defects at once.  The bit positions are assigned as follows\:  etherWisFarEndPayloadDefect(0)    A far end payload defect (i.e., far end    PLM\-P or LCD\-P) is currently being signaled    in G1 bits 5\-7.  etherWisFarEndServerDefect(1)    A far end server defect (i.e., far end    LOP\-P or AIS\-P) is currently being signaled    in G1 bits 5\-7.  Note\:  when this bit is set,    sonetPathSTSRDI MUST be set in the corresponding    instance of sonetPathCurrentStatus
            	**type**\:   :py:class:`Etherwisfarendpathcurrentstatus <ydk.models.cisco_ios_xe.ETHER_WIS.EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry.Etherwisfarendpathcurrentstatus>`
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry, self).__init__()

                self.yang_name = "etherWisFarEndPathCurrentEntry"
                self.yang_parent_name = "etherWisFarEndPathCurrentTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.etherwisfarendpathcurrentstatus = YLeaf(YType.bits, "etherWisFarEndPathCurrentStatus")

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
                                "etherwisfarendpathcurrentstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.etherwisfarendpathcurrentstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.etherwisfarendpathcurrentstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "etherWisFarEndPathCurrentEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ETHER-WIS:ETHER-WIS/etherWisFarEndPathCurrentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.etherwisfarendpathcurrentstatus.is_set or self.etherwisfarendpathcurrentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.etherwisfarendpathcurrentstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "etherWisFarEndPathCurrentStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "etherWisFarEndPathCurrentStatus"):
                    self.etherwisfarendpathcurrentstatus[value] = True

        def has_data(self):
            for c in self.etherwisfarendpathcurrententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.etherwisfarendpathcurrententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "etherWisFarEndPathCurrentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ETHER-WIS:ETHER-WIS/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "etherWisFarEndPathCurrentEntry"):
                for c in self.etherwisfarendpathcurrententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.etherwisfarendpathcurrententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "etherWisFarEndPathCurrentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.etherwisdevicetable is not None and self.etherwisdevicetable.has_data()) or
            (self.etherwisfarendpathcurrenttable is not None and self.etherwisfarendpathcurrenttable.has_data()) or
            (self.etherwispathcurrenttable is not None and self.etherwispathcurrenttable.has_data()) or
            (self.etherwissectioncurrenttable is not None and self.etherwissectioncurrenttable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.etherwisdevicetable is not None and self.etherwisdevicetable.has_operation()) or
            (self.etherwisfarendpathcurrenttable is not None and self.etherwisfarendpathcurrenttable.has_operation()) or
            (self.etherwispathcurrenttable is not None and self.etherwispathcurrenttable.has_operation()) or
            (self.etherwissectioncurrenttable is not None and self.etherwissectioncurrenttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ETHER-WIS:ETHER-WIS" + path_buffer

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

        if (child_yang_name == "etherWisDeviceTable"):
            if (self.etherwisdevicetable is None):
                self.etherwisdevicetable = EtherWis.Etherwisdevicetable()
                self.etherwisdevicetable.parent = self
                self._children_name_map["etherwisdevicetable"] = "etherWisDeviceTable"
            return self.etherwisdevicetable

        if (child_yang_name == "etherWisFarEndPathCurrentTable"):
            if (self.etherwisfarendpathcurrenttable is None):
                self.etherwisfarendpathcurrenttable = EtherWis.Etherwisfarendpathcurrenttable()
                self.etherwisfarendpathcurrenttable.parent = self
                self._children_name_map["etherwisfarendpathcurrenttable"] = "etherWisFarEndPathCurrentTable"
            return self.etherwisfarendpathcurrenttable

        if (child_yang_name == "etherWisPathCurrentTable"):
            if (self.etherwispathcurrenttable is None):
                self.etherwispathcurrenttable = EtherWis.Etherwispathcurrenttable()
                self.etherwispathcurrenttable.parent = self
                self._children_name_map["etherwispathcurrenttable"] = "etherWisPathCurrentTable"
            return self.etherwispathcurrenttable

        if (child_yang_name == "etherWisSectionCurrentTable"):
            if (self.etherwissectioncurrenttable is None):
                self.etherwissectioncurrenttable = EtherWis.Etherwissectioncurrenttable()
                self.etherwissectioncurrenttable.parent = self
                self._children_name_map["etherwissectioncurrenttable"] = "etherWisSectionCurrentTable"
            return self.etherwissectioncurrenttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "etherWisDeviceTable" or name == "etherWisFarEndPathCurrentTable" or name == "etherWisPathCurrentTable" or name == "etherWisSectionCurrentTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EtherWis()
        return self._top_entity


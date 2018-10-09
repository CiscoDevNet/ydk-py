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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ETHERWIS(Entity):
    """
    
    
    .. attribute:: etherwisdevicetable
    
    	The table for Ethernet WIS devices
    	**type**\:  :py:class:`EtherWisDeviceTable <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisDeviceTable>`
    
    .. attribute:: etherwissectioncurrenttable
    
    	The table for the current state of Ethernet WIS sections
    	**type**\:  :py:class:`EtherWisSectionCurrentTable <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisSectionCurrentTable>`
    
    .. attribute:: etherwispathcurrenttable
    
    	The table for the current state of Ethernet WIS paths
    	**type**\:  :py:class:`EtherWisPathCurrentTable <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisPathCurrentTable>`
    
    .. attribute:: etherwisfarendpathcurrenttable
    
    	The table for the current far\-end state of Ethernet WIS paths
    	**type**\:  :py:class:`EtherWisFarEndPathCurrentTable <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisFarEndPathCurrentTable>`
    
    

    """

    _prefix = 'ETHER-WIS'
    _revision = '2003-09-19'

    def __init__(self):
        super(ETHERWIS, self).__init__()
        self._top_entity = None

        self.yang_name = "ETHER-WIS"
        self.yang_parent_name = "ETHER-WIS"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("etherWisDeviceTable", ("etherwisdevicetable", ETHERWIS.EtherWisDeviceTable)), ("etherWisSectionCurrentTable", ("etherwissectioncurrenttable", ETHERWIS.EtherWisSectionCurrentTable)), ("etherWisPathCurrentTable", ("etherwispathcurrenttable", ETHERWIS.EtherWisPathCurrentTable)), ("etherWisFarEndPathCurrentTable", ("etherwisfarendpathcurrenttable", ETHERWIS.EtherWisFarEndPathCurrentTable))])
        self._leafs = OrderedDict()

        self.etherwisdevicetable = ETHERWIS.EtherWisDeviceTable()
        self.etherwisdevicetable.parent = self
        self._children_name_map["etherwisdevicetable"] = "etherWisDeviceTable"

        self.etherwissectioncurrenttable = ETHERWIS.EtherWisSectionCurrentTable()
        self.etherwissectioncurrenttable.parent = self
        self._children_name_map["etherwissectioncurrenttable"] = "etherWisSectionCurrentTable"

        self.etherwispathcurrenttable = ETHERWIS.EtherWisPathCurrentTable()
        self.etherwispathcurrenttable.parent = self
        self._children_name_map["etherwispathcurrenttable"] = "etherWisPathCurrentTable"

        self.etherwisfarendpathcurrenttable = ETHERWIS.EtherWisFarEndPathCurrentTable()
        self.etherwisfarendpathcurrenttable.parent = self
        self._children_name_map["etherwisfarendpathcurrenttable"] = "etherWisFarEndPathCurrentTable"
        self._segment_path = lambda: "ETHER-WIS:ETHER-WIS"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ETHERWIS, [], name, value)


    class EtherWisDeviceTable(Entity):
        """
        The table for Ethernet WIS devices
        
        .. attribute:: etherwisdeviceentry
        
        	An entry in the Ethernet WIS device table.  For each instance of this object there MUST be a corresponding instance of sonetMediumEntry
        	**type**\: list of  		 :py:class:`EtherWisDeviceEntry <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(ETHERWIS.EtherWisDeviceTable, self).__init__()

            self.yang_name = "etherWisDeviceTable"
            self.yang_parent_name = "ETHER-WIS"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("etherWisDeviceEntry", ("etherwisdeviceentry", ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry))])
            self._leafs = OrderedDict()

            self.etherwisdeviceentry = YList(self)
            self._segment_path = lambda: "etherWisDeviceTable"
            self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ETHERWIS.EtherWisDeviceTable, [], name, value)


        class EtherWisDeviceEntry(Entity):
            """
            An entry in the Ethernet WIS device table.  For each
            instance of this object there MUST be a corresponding
            instance of sonetMediumEntry.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: etherwisdevicetxtestpatternmode
            
            	This variable controls the transmit test pattern mode. The value none(1) puts the the WIS transmit path into the normal operating mode.  The value squareWave(2) puts the WIS transmit path into the square wave test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.1. The value prbs31(3) puts the WIS transmit path into the PRBS31 test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value mixedFrequency(4) puts the WIS transmit path into the mixed frequency test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.3. Any attempt to set this object to a value other than none(1) when the corresponding instance of ifAdminStatus has the value up(1) MUST be rejected with the error inconsistentValue, and any attempt to set the corresponding instance of ifAdminStatus to the value up(1) when an instance of this object has a value other than none(1) MUST be rejected with the error inconsistentValue
            	**type**\:  :py:class:`EtherWisDeviceTxTestPatternMode <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceTxTestPatternMode>`
            
            .. attribute:: etherwisdevicerxtestpatternmode
            
            	This variable controls the receive test pattern mode. The value none(1) puts the the WIS receive path into the normal operating mode.  The value prbs31(3) puts the WIS receive path into the PRBS31 test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value mixedFrequency(4) puts the WIS receive path into the mixed frequency test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.3.  Any attempt to set this object to a value other than none(1) when the corresponding instance of ifAdminStatus has the value up(1) MUST be rejected with the error inconsistentValue, and any attempt to set the corresponding instance of ifAdminStatus to the value up(1) when an instance of this object has a value other than none(1) MUST be rejected with the error inconsistentValue
            	**type**\:  :py:class:`EtherWisDeviceRxTestPatternMode <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceRxTestPatternMode>`
            
            .. attribute:: etherwisdevicerxtestpatternerrors
            
            	This object counts the number of errors detected when the WIS receive path is operating in the PRBS31 test pattern mode.  It is reset to zero when the WIS receive path initially enters that mode, and it increments each time the PRBS pattern checker detects an error as described in [IEEE 802.3 Std.] subclause 50.3.8.2 unless its value is 65535, in which case it remains unchanged.  This object is writeable so that it may be reset upon explicit request of a command generator application while the WIS receive path continues to operate in PRBS31 test pattern mode
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry, self).__init__()

                self.yang_name = "etherWisDeviceEntry"
                self.yang_parent_name = "etherWisDeviceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('etherwisdevicetxtestpatternmode', (YLeaf(YType.enumeration, 'etherWisDeviceTxTestPatternMode'), [('ydk.models.cisco_ios_xe.ETHER_WIS', 'ETHERWIS', 'EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceTxTestPatternMode')])),
                    ('etherwisdevicerxtestpatternmode', (YLeaf(YType.enumeration, 'etherWisDeviceRxTestPatternMode'), [('ydk.models.cisco_ios_xe.ETHER_WIS', 'ETHERWIS', 'EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceRxTestPatternMode')])),
                    ('etherwisdevicerxtestpatternerrors', (YLeaf(YType.uint32, 'etherWisDeviceRxTestPatternErrors'), ['int'])),
                ])
                self.ifindex = None
                self.etherwisdevicetxtestpatternmode = None
                self.etherwisdevicerxtestpatternmode = None
                self.etherwisdevicerxtestpatternerrors = None
                self._segment_path = lambda: "etherWisDeviceEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/etherWisDeviceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry, ['ifindex', 'etherwisdevicetxtestpatternmode', 'etherwisdevicerxtestpatternmode', 'etherwisdevicerxtestpatternerrors'], name, value)

            class EtherWisDeviceRxTestPatternMode(Enum):
                """
                EtherWisDeviceRxTestPatternMode (Enum Class)

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


            class EtherWisDeviceTxTestPatternMode(Enum):
                """
                EtherWisDeviceTxTestPatternMode (Enum Class)

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



    class EtherWisSectionCurrentTable(Entity):
        """
        The table for the current state of Ethernet WIS sections.
        
        .. attribute:: etherwissectioncurrententry
        
        	An entry in the etherWisSectionCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetSectionCurrentEntry
        	**type**\: list of  		 :py:class:`EtherWisSectionCurrentEntry <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(ETHERWIS.EtherWisSectionCurrentTable, self).__init__()

            self.yang_name = "etherWisSectionCurrentTable"
            self.yang_parent_name = "ETHER-WIS"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("etherWisSectionCurrentEntry", ("etherwissectioncurrententry", ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry))])
            self._leafs = OrderedDict()

            self.etherwissectioncurrententry = YList(self)
            self._segment_path = lambda: "etherWisSectionCurrentTable"
            self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ETHERWIS.EtherWisSectionCurrentTable, [], name, value)


        class EtherWisSectionCurrentEntry(Entity):
            """
            An entry in the etherWisSectionCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetSectionCurrentEntry.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: etherwissectioncurrentj0transmitted
            
            	This is the 16\-octet section trace message that is transmitted in the J0 byte.  The value SHOULD be '89'h followed by fifteen octets of '00'h (or some cyclic shift thereof) when the section trace function is not used, and the implementation SHOULD use that value (or a cyclic shift thereof) as a default if no other value has been set
            	**type**\: str
            
            	**length:** 16
            
            .. attribute:: etherwissectioncurrentj0received
            
            	This is the 16\-octet section trace message that was most recently received in the J0 byte
            	**type**\: str
            
            	**length:** 16
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry, self).__init__()

                self.yang_name = "etherWisSectionCurrentEntry"
                self.yang_parent_name = "etherWisSectionCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('etherwissectioncurrentj0transmitted', (YLeaf(YType.str, 'etherWisSectionCurrentJ0Transmitted'), ['str'])),
                    ('etherwissectioncurrentj0received', (YLeaf(YType.str, 'etherWisSectionCurrentJ0Received'), ['str'])),
                ])
                self.ifindex = None
                self.etherwissectioncurrentj0transmitted = None
                self.etherwissectioncurrentj0received = None
                self._segment_path = lambda: "etherWisSectionCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/etherWisSectionCurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry, ['ifindex', 'etherwissectioncurrentj0transmitted', 'etherwissectioncurrentj0received'], name, value)


    class EtherWisPathCurrentTable(Entity):
        """
        The table for the current state of Ethernet WIS paths.
        
        .. attribute:: etherwispathcurrententry
        
        	An entry in the etherWisPathCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetPathCurrentEntry
        	**type**\: list of  		 :py:class:`EtherWisPathCurrentEntry <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(ETHERWIS.EtherWisPathCurrentTable, self).__init__()

            self.yang_name = "etherWisPathCurrentTable"
            self.yang_parent_name = "ETHER-WIS"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("etherWisPathCurrentEntry", ("etherwispathcurrententry", ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry))])
            self._leafs = OrderedDict()

            self.etherwispathcurrententry = YList(self)
            self._segment_path = lambda: "etherWisPathCurrentTable"
            self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ETHERWIS.EtherWisPathCurrentTable, [], name, value)


        class EtherWisPathCurrentEntry(Entity):
            """
            An entry in the etherWisPathCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetPathCurrentEntry.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: etherwispathcurrentstatus
            
            	This variable indicates the current status of the path payload with a bit map that can indicate multiple defects at once.  The bit positions are assigned as follows\:  etherWisPathLOP(0)    This bit is set to indicate that an    LOP\-P (Loss of Pointer \- Path) defect    is being experienced.  Note\:  when this    bit is set, sonetPathSTSLOP MUST be set    in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathAIS(1)    This bit is set to indicate that an    AIS\-P (Alarm Indication Signal \- Path)    defect is being experienced.  Note\:  when    this bit is set, sonetPathSTSAIS MUST be    set in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathPLM(1)    This bit is set to indicate that a    PLM\-P (Payload Label Mismatch \- Path)    defect is being experienced.  Note\:  when    this bit is set, sonetPathSignalLabelMismatch    MUST be set in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathLCD(3)    This bit is set to indicate that an    LCD\-P (Loss of Codegroup Delination \- Path)    defect is being experienced.  Since this    defect is detected by the PCS and not by    the path layer itself, there is no    corresponding bit in sonetPathCurrentStatus
            	**type**\:  :py:class:`EtherWisPathCurrentStatus <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry.EtherWisPathCurrentStatus>`
            
            .. attribute:: etherwispathcurrentj1transmitted
            
            	This is the 16\-octet path trace message that is transmitted in the J1 byte.  The value SHOULD be '89'h followed by fifteen octets of '00'h (or some cyclic shift thereof) when the path trace function is not used, and the implementation SHOULD use that value (or a cyclic shift thereof) as a default if no other value has been set
            	**type**\: str
            
            	**length:** 16
            
            .. attribute:: etherwispathcurrentj1received
            
            	This is the 16\-octet path trace message that was most recently received in the J1 byte
            	**type**\: str
            
            	**length:** 16
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry, self).__init__()

                self.yang_name = "etherWisPathCurrentEntry"
                self.yang_parent_name = "etherWisPathCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('etherwispathcurrentstatus', (YLeaf(YType.bits, 'etherWisPathCurrentStatus'), ['Bits'])),
                    ('etherwispathcurrentj1transmitted', (YLeaf(YType.str, 'etherWisPathCurrentJ1Transmitted'), ['str'])),
                    ('etherwispathcurrentj1received', (YLeaf(YType.str, 'etherWisPathCurrentJ1Received'), ['str'])),
                ])
                self.ifindex = None
                self.etherwispathcurrentstatus = Bits()
                self.etherwispathcurrentj1transmitted = None
                self.etherwispathcurrentj1received = None
                self._segment_path = lambda: "etherWisPathCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/etherWisPathCurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry, ['ifindex', 'etherwispathcurrentstatus', 'etherwispathcurrentj1transmitted', 'etherwispathcurrentj1received'], name, value)


    class EtherWisFarEndPathCurrentTable(Entity):
        """
        The table for the current far\-end state of Ethernet WIS
        paths.
        
        .. attribute:: etherwisfarendpathcurrententry
        
        	An entry in the etherWisFarEndPathCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetFarEndPathCurrentEntry
        	**type**\: list of  		 :py:class:`EtherWisFarEndPathCurrentEntry <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry>`
        
        

        """

        _prefix = 'ETHER-WIS'
        _revision = '2003-09-19'

        def __init__(self):
            super(ETHERWIS.EtherWisFarEndPathCurrentTable, self).__init__()

            self.yang_name = "etherWisFarEndPathCurrentTable"
            self.yang_parent_name = "ETHER-WIS"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("etherWisFarEndPathCurrentEntry", ("etherwisfarendpathcurrententry", ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry))])
            self._leafs = OrderedDict()

            self.etherwisfarendpathcurrententry = YList(self)
            self._segment_path = lambda: "etherWisFarEndPathCurrentTable"
            self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ETHERWIS.EtherWisFarEndPathCurrentTable, [], name, value)


        class EtherWisFarEndPathCurrentEntry(Entity):
            """
            An entry in the etherWisFarEndPathCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetFarEndPathCurrentEntry.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            .. attribute:: etherwisfarendpathcurrentstatus
            
            	This variable indicates the current status at the far end of the path using a bit map that can indicate multiple defects at once.  The bit positions are assigned as follows\:  etherWisFarEndPayloadDefect(0)    A far end payload defect (i.e., far end    PLM\-P or LCD\-P) is currently being signaled    in G1 bits 5\-7.  etherWisFarEndServerDefect(1)    A far end server defect (i.e., far end    LOP\-P or AIS\-P) is currently being signaled    in G1 bits 5\-7.  Note\:  when this bit is set,    sonetPathSTSRDI MUST be set in the corresponding    instance of sonetPathCurrentStatus
            	**type**\:  :py:class:`EtherWisFarEndPathCurrentStatus <ydk.models.cisco_ios_xe.ETHER_WIS.ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry.EtherWisFarEndPathCurrentStatus>`
            
            

            """

            _prefix = 'ETHER-WIS'
            _revision = '2003-09-19'

            def __init__(self):
                super(ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry, self).__init__()

                self.yang_name = "etherWisFarEndPathCurrentEntry"
                self.yang_parent_name = "etherWisFarEndPathCurrentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('etherwisfarendpathcurrentstatus', (YLeaf(YType.bits, 'etherWisFarEndPathCurrentStatus'), ['Bits'])),
                ])
                self.ifindex = None
                self.etherwisfarendpathcurrentstatus = Bits()
                self._segment_path = lambda: "etherWisFarEndPathCurrentEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "ETHER-WIS:ETHER-WIS/etherWisFarEndPathCurrentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry, ['ifindex', 'etherwisfarendpathcurrentstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = ETHERWIS()
        return self._top_entity


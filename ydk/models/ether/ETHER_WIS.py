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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class ETHERWIS(object):
    """
    
    
    .. attribute:: etherwisdevicetable
    
    	The table for Ethernet WIS devices
    	**type**\: :py:class:`EtherWisDeviceTable <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisDeviceTable>`
    
    .. attribute:: etherwisfarendpathcurrenttable
    
    	The table for the current far\-end state of Ethernet WIS paths
    	**type**\: :py:class:`EtherWisFarEndPathCurrentTable <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisFarEndPathCurrentTable>`
    
    .. attribute:: etherwispathcurrenttable
    
    	The table for the current state of Ethernet WIS paths
    	**type**\: :py:class:`EtherWisPathCurrentTable <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisPathCurrentTable>`
    
    .. attribute:: etherwissectioncurrenttable
    
    	The table for the current state of Ethernet WIS sections
    	**type**\: :py:class:`EtherWisSectionCurrentTable <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisSectionCurrentTable>`
    
    

    """

    _prefix = 'ether-wis'
    _revision = '2003-09-19'

    def __init__(self):
        self.etherwisdevicetable = ETHERWIS.EtherWisDeviceTable()
        self.etherwisdevicetable.parent = self
        self.etherwisfarendpathcurrenttable = ETHERWIS.EtherWisFarEndPathCurrentTable()
        self.etherwisfarendpathcurrenttable.parent = self
        self.etherwispathcurrenttable = ETHERWIS.EtherWisPathCurrentTable()
        self.etherwispathcurrenttable.parent = self
        self.etherwissectioncurrenttable = ETHERWIS.EtherWisSectionCurrentTable()
        self.etherwissectioncurrenttable.parent = self


    class EtherWisDeviceTable(object):
        """
        The table for Ethernet WIS devices
        
        .. attribute:: etherwisdeviceentry
        
        	An entry in the Ethernet WIS device table.  For each instance of this object there MUST be a corresponding instance of sonetMediumEntry
        	**type**\: list of :py:class:`EtherWisDeviceEntry <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry>`
        
        

        """

        _prefix = 'ether-wis'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.etherwisdeviceentry = YList()
            self.etherwisdeviceentry.parent = self
            self.etherwisdeviceentry.name = 'etherwisdeviceentry'


        class EtherWisDeviceEntry(object):
            """
            An entry in the Ethernet WIS device table.  For each
            instance of this object there MUST be a corresponding
            instance of sonetMediumEntry.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: etherwisdevicerxtestpatternerrors
            
            	This object counts the number of errors detected when the WIS receive path is operating in the PRBS31 test pattern mode.  It is reset to zero when the WIS receive path initially enters that mode, and it increments each time the PRBS pattern checker detects an error as described in [IEEE 802.3 Std.] subclause 50.3.8.2 unless its value is 65535, in which case it remains unchanged.  This object is writeable so that it may be reset upon explicit request of a command generator application while the WIS receive path continues to operate in PRBS31 test pattern mode
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: etherwisdevicerxtestpatternmode
            
            	This variable controls the receive test pattern mode. The value none(1) puts the the WIS receive path into the normal operating mode.  The value prbs31(3) puts the WIS receive path into the PRBS31 test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value mixedFrequency(4) puts the WIS receive path into the mixed frequency test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.3.  Any attempt to set this object to a value other than none(1) when the corresponding instance of ifAdminStatus has the value up(1) MUST be rejected with the error inconsistentValue, and any attempt to set the corresponding instance of ifAdminStatus to the value up(1) when an instance of this object has a value other than none(1) MUST be rejected with the error inconsistentValue
            	**type**\: :py:class:`EtherWisDeviceRxTestPatternMode_Enum <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceRxTestPatternMode_Enum>`
            
            .. attribute:: etherwisdevicetxtestpatternmode
            
            	This variable controls the transmit test pattern mode. The value none(1) puts the the WIS transmit path into the normal operating mode.  The value squareWave(2) puts the WIS transmit path into the square wave test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.1. The value prbs31(3) puts the WIS transmit path into the PRBS31 test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.2.  The value mixedFrequency(4) puts the WIS transmit path into the mixed frequency test pattern mode described in [IEEE 802.3 Std.] subclause 50.3.8.3. Any attempt to set this object to a value other than none(1) when the corresponding instance of ifAdminStatus has the value up(1) MUST be rejected with the error inconsistentValue, and any attempt to set the corresponding instance of ifAdminStatus to the value up(1) when an instance of this object has a value other than none(1) MUST be rejected with the error inconsistentValue
            	**type**\: :py:class:`EtherWisDeviceTxTestPatternMode_Enum <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceTxTestPatternMode_Enum>`
            
            

            """

            _prefix = 'ether-wis'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.etherwisdevicerxtestpatternerrors = None
                self.etherwisdevicerxtestpatternmode = None
                self.etherwisdevicetxtestpatternmode = None

            class EtherWisDeviceRxTestPatternMode_Enum(Enum):
                """
                EtherWisDeviceRxTestPatternMode_Enum

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

                """

                NONE = 1

                PRBS31 = 3

                MIXEDFREQUENCY = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.ether._meta import _ETHER_WIS as meta
                    return meta._meta_table['ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceRxTestPatternMode_Enum']


            class EtherWisDeviceTxTestPatternMode_Enum(Enum):
                """
                EtherWisDeviceTxTestPatternMode_Enum

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

                """

                NONE = 1

                SQUAREWAVE = 2

                PRBS31 = 3

                MIXEDFREQUENCY = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.ether._meta import _ETHER_WIS as meta
                    return meta._meta_table['ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceTxTestPatternMode_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisDeviceTable/ETHER-WIS:etherWisDeviceEntry[ETHER-WIS:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.etherwisdevicerxtestpatternerrors is not None:
                    return True

                if self.etherwisdevicerxtestpatternmode is not None:
                    return True

                if self.etherwisdevicetxtestpatternmode is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ether._meta import _ETHER_WIS as meta
                return meta._meta_table['ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisDeviceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.etherwisdeviceentry is not None:
                for child_ref in self.etherwisdeviceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ether._meta import _ETHER_WIS as meta
            return meta._meta_table['ETHERWIS.EtherWisDeviceTable']['meta_info']


    class EtherWisFarEndPathCurrentTable(object):
        """
        The table for the current far\-end state of Ethernet WIS
        paths.
        
        .. attribute:: etherwisfarendpathcurrententry
        
        	An entry in the etherWisFarEndPathCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetFarEndPathCurrentEntry
        	**type**\: list of :py:class:`EtherWisFarEndPathCurrentEntry <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry>`
        
        

        """

        _prefix = 'ether-wis'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.etherwisfarendpathcurrententry = YList()
            self.etherwisfarendpathcurrententry.parent = self
            self.etherwisfarendpathcurrententry.name = 'etherwisfarendpathcurrententry'


        class EtherWisFarEndPathCurrentEntry(object):
            """
            An entry in the etherWisFarEndPathCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetFarEndPathCurrentEntry.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: etherwisfarendpathcurrentstatus
            
            	This variable indicates the current status at the far end of the path using a bit map that can indicate multiple defects at once.  The bit positions are assigned as follows\:  etherWisFarEndPayloadDefect(0)    A far end payload defect (i.e., far end    PLM\-P or LCD\-P) is currently being signaled    in G1 bits 5\-7.  etherWisFarEndServerDefect(1)    A far end server defect (i.e., far end    LOP\-P or AIS\-P) is currently being signaled    in G1 bits 5\-7.  Note\:  when this bit is set,    sonetPathSTSRDI MUST be set in the corresponding    instance of sonetPathCurrentStatus
            	**type**\: :py:class:`EtherWisFarEndPathCurrentStatus_Bits <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry.EtherWisFarEndPathCurrentStatus_Bits>`
            
            

            """

            _prefix = 'ether-wis'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.etherwisfarendpathcurrentstatus = ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry.EtherWisFarEndPathCurrentStatus_Bits()

            class EtherWisFarEndPathCurrentStatus_Bits(FixedBitsDict):
                """
                EtherWisFarEndPathCurrentStatus_Bits

                This variable indicates the current status at the
                far end of the path using a bit map that can indicate
                multiple defects at once.  The bit positions are
                assigned as follows\:
                
                etherWisFarEndPayloadDefect(0)
                   A far end payload defect (i.e., far end
                   PLM\-P or LCD\-P) is currently being signaled
                   in G1 bits 5\-7.
                
                etherWisFarEndServerDefect(1)
                   A far end server defect (i.e., far end
                   LOP\-P or AIS\-P) is currently being signaled
                   in G1 bits 5\-7.  Note\:  when this bit is set,
                   sonetPathSTSRDI MUST be set in the corresponding
                   instance of sonetPathCurrentStatus.
                Keys are:- etherWisFarEndServerDefect , etherWisFarEndPayloadDefect

                """

                def __init__(self):
                    self._dictionary = { 
                        'etherWisFarEndServerDefect':False,
                        'etherWisFarEndPayloadDefect':False,
                    }
                    self._pos_map = { 
                        'etherWisFarEndServerDefect':1,
                        'etherWisFarEndPayloadDefect':0,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisFarEndPathCurrentTable/ETHER-WIS:etherWisFarEndPathCurrentEntry[ETHER-WIS:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.etherwisfarendpathcurrentstatus is not None:
                    if self.etherwisfarendpathcurrentstatus._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ether._meta import _ETHER_WIS as meta
                return meta._meta_table['ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisFarEndPathCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.etherwisfarendpathcurrententry is not None:
                for child_ref in self.etherwisfarendpathcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ether._meta import _ETHER_WIS as meta
            return meta._meta_table['ETHERWIS.EtherWisFarEndPathCurrentTable']['meta_info']


    class EtherWisPathCurrentTable(object):
        """
        The table for the current state of Ethernet WIS paths.
        
        .. attribute:: etherwispathcurrententry
        
        	An entry in the etherWisPathCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetPathCurrentEntry
        	**type**\: list of :py:class:`EtherWisPathCurrentEntry <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry>`
        
        

        """

        _prefix = 'ether-wis'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.etherwispathcurrententry = YList()
            self.etherwispathcurrententry.parent = self
            self.etherwispathcurrententry.name = 'etherwispathcurrententry'


        class EtherWisPathCurrentEntry(object):
            """
            An entry in the etherWisPathCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetPathCurrentEntry.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: etherwispathcurrentj1received
            
            	This is the 16\-octet path trace message that was most recently received in the J1 byte
            	**type**\: str
            
            	**range:** 16
            
            .. attribute:: etherwispathcurrentj1transmitted
            
            	This is the 16\-octet path trace message that is transmitted in the J1 byte.  The value SHOULD be '89'h followed by fifteen octets of '00'h (or some cyclic shift thereof) when the path trace function is not used, and the implementation SHOULD use that value (or a cyclic shift thereof) as a default if no other value has been set
            	**type**\: str
            
            	**range:** 16
            
            .. attribute:: etherwispathcurrentstatus
            
            	This variable indicates the current status of the path payload with a bit map that can indicate multiple defects at once.  The bit positions are assigned as follows\:  etherWisPathLOP(0)    This bit is set to indicate that an    LOP\-P (Loss of Pointer \- Path) defect    is being experienced.  Note\:  when this    bit is set, sonetPathSTSLOP MUST be set    in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathAIS(1)    This bit is set to indicate that an    AIS\-P (Alarm Indication Signal \- Path)    defect is being experienced.  Note\:  when    this bit is set, sonetPathSTSAIS MUST be    set in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathPLM(1)    This bit is set to indicate that a    PLM\-P (Payload Label Mismatch \- Path)    defect is being experienced.  Note\:  when    this bit is set, sonetPathSignalLabelMismatch    MUST be set in the corresponding instance of    sonetPathCurrentStatus.  etherWisPathLCD(3)    This bit is set to indicate that an    LCD\-P (Loss of Codegroup Delination \- Path)    defect is being experienced.  Since this    defect is detected by the PCS and not by    the path layer itself, there is no    corresponding bit in sonetPathCurrentStatus
            	**type**\: :py:class:`EtherWisPathCurrentStatus_Bits <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry.EtherWisPathCurrentStatus_Bits>`
            
            

            """

            _prefix = 'ether-wis'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.etherwispathcurrentj1received = None
                self.etherwispathcurrentj1transmitted = None
                self.etherwispathcurrentstatus = ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry.EtherWisPathCurrentStatus_Bits()

            class EtherWisPathCurrentStatus_Bits(FixedBitsDict):
                """
                EtherWisPathCurrentStatus_Bits

                This variable indicates the current status of the
                path payload with a bit map that can indicate multiple
                defects at once.  The bit positions are assigned as
                follows\:
                
                etherWisPathLOP(0)
                   This bit is set to indicate that an
                   LOP\-P (Loss of Pointer \- Path) defect
                   is being experienced.  Note\:  when this
                   bit is set, sonetPathSTSLOP MUST be set
                   in the corresponding instance of
                   sonetPathCurrentStatus.
                
                etherWisPathAIS(1)
                   This bit is set to indicate that an
                   AIS\-P (Alarm Indication Signal \- Path)
                   defect is being experienced.  Note\:  when
                   this bit is set, sonetPathSTSAIS MUST be
                   set in the corresponding instance of
                   sonetPathCurrentStatus.
                
                etherWisPathPLM(1)
                   This bit is set to indicate that a
                   PLM\-P (Payload Label Mismatch \- Path)
                   defect is being experienced.  Note\:  when
                   this bit is set, sonetPathSignalLabelMismatch
                   MUST be set in the corresponding instance of
                   sonetPathCurrentStatus.
                
                etherWisPathLCD(3)
                   This bit is set to indicate that an
                   LCD\-P (Loss of Codegroup Delination \- Path)
                   defect is being experienced.  Since this
                   defect is detected by the PCS and not by
                   the path layer itself, there is no
                   corresponding bit in sonetPathCurrentStatus.
                Keys are:- etherWisPathAIS , etherWisPathPLM , etherWisPathLCD , etherWisPathLOP

                """

                def __init__(self):
                    self._dictionary = { 
                        'etherWisPathAIS':False,
                        'etherWisPathPLM':False,
                        'etherWisPathLCD':False,
                        'etherWisPathLOP':False,
                    }
                    self._pos_map = { 
                        'etherWisPathAIS':1,
                        'etherWisPathPLM':2,
                        'etherWisPathLCD':3,
                        'etherWisPathLOP':0,
                    }

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisPathCurrentTable/ETHER-WIS:etherWisPathCurrentEntry[ETHER-WIS:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.etherwispathcurrentj1received is not None:
                    return True

                if self.etherwispathcurrentj1transmitted is not None:
                    return True

                if self.etherwispathcurrentstatus is not None:
                    if self.etherwispathcurrentstatus._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ether._meta import _ETHER_WIS as meta
                return meta._meta_table['ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisPathCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.etherwispathcurrententry is not None:
                for child_ref in self.etherwispathcurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ether._meta import _ETHER_WIS as meta
            return meta._meta_table['ETHERWIS.EtherWisPathCurrentTable']['meta_info']


    class EtherWisSectionCurrentTable(object):
        """
        The table for the current state of Ethernet WIS sections.
        
        .. attribute:: etherwissectioncurrententry
        
        	An entry in the etherWisSectionCurrentTable.  For each instance of this object there MUST be a corresponding instance of sonetSectionCurrentEntry
        	**type**\: list of :py:class:`EtherWisSectionCurrentEntry <ydk.models.ether.ETHER_WIS.ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry>`
        
        

        """

        _prefix = 'ether-wis'
        _revision = '2003-09-19'

        def __init__(self):
            self.parent = None
            self.etherwissectioncurrententry = YList()
            self.etherwissectioncurrententry.parent = self
            self.etherwissectioncurrententry.name = 'etherwissectioncurrententry'


        class EtherWisSectionCurrentEntry(object):
            """
            An entry in the etherWisSectionCurrentTable.  For each
            instance of this object there MUST be a corresponding
            instance of sonetSectionCurrentEntry.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: etherwissectioncurrentj0received
            
            	This is the 16\-octet section trace message that was most recently received in the J0 byte
            	**type**\: str
            
            	**range:** 16
            
            .. attribute:: etherwissectioncurrentj0transmitted
            
            	This is the 16\-octet section trace message that is transmitted in the J0 byte.  The value SHOULD be '89'h followed by fifteen octets of '00'h (or some cyclic shift thereof) when the section trace function is not used, and the implementation SHOULD use that value (or a cyclic shift thereof) as a default if no other value has been set
            	**type**\: str
            
            	**range:** 16
            
            

            """

            _prefix = 'ether-wis'
            _revision = '2003-09-19'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.etherwissectioncurrentj0received = None
                self.etherwissectioncurrentj0transmitted = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisSectionCurrentTable/ETHER-WIS:etherWisSectionCurrentEntry[ETHER-WIS:ifIndex = ' + str(self.ifindex) + ']'

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

                if self.etherwissectioncurrentj0received is not None:
                    return True

                if self.etherwissectioncurrentj0transmitted is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ether._meta import _ETHER_WIS as meta
                return meta._meta_table['ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry']['meta_info']

        @property
        def _common_path(self):

            return '/ETHER-WIS:ETHER-WIS/ETHER-WIS:etherWisSectionCurrentTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.etherwissectioncurrententry is not None:
                for child_ref in self.etherwissectioncurrententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ether._meta import _ETHER_WIS as meta
            return meta._meta_table['ETHERWIS.EtherWisSectionCurrentTable']['meta_info']

    @property
    def _common_path(self):

        return '/ETHER-WIS:ETHER-WIS'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.etherwisdevicetable is not None and self.etherwisdevicetable._has_data():
            return True

        if self.etherwisdevicetable is not None and self.etherwisdevicetable.is_presence():
            return True

        if self.etherwisfarendpathcurrenttable is not None and self.etherwisfarendpathcurrenttable._has_data():
            return True

        if self.etherwisfarendpathcurrenttable is not None and self.etherwisfarendpathcurrenttable.is_presence():
            return True

        if self.etherwispathcurrenttable is not None and self.etherwispathcurrenttable._has_data():
            return True

        if self.etherwispathcurrenttable is not None and self.etherwispathcurrenttable.is_presence():
            return True

        if self.etherwissectioncurrenttable is not None and self.etherwissectioncurrenttable._has_data():
            return True

        if self.etherwissectioncurrenttable is not None and self.etherwissectioncurrenttable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ether._meta import _ETHER_WIS as meta
        return meta._meta_table['ETHERWIS']['meta_info']



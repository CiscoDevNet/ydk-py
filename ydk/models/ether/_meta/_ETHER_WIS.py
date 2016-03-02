


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceRxTestPatternMode_Enum' : _MetaInfoEnum('EtherWisDeviceRxTestPatternMode_Enum', 'ydk.models.ether.ETHER_WIS',
        {
            'none':'NONE',
            'prbs31':'PRBS31',
            'mixedFrequency':'MIXEDFREQUENCY',
        }, 'ETHER-WIS', _yang_ns._namespaces['ETHER-WIS']),
    'ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceTxTestPatternMode_Enum' : _MetaInfoEnum('EtherWisDeviceTxTestPatternMode_Enum', 'ydk.models.ether.ETHER_WIS',
        {
            'none':'NONE',
            'squareWave':'SQUAREWAVE',
            'prbs31':'PRBS31',
            'mixedFrequency':'MIXEDFREQUENCY',
        }, 'ETHER-WIS', _yang_ns._namespaces['ETHER-WIS']),
    'ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ETHER-WIS', True),
            _MetaInfoClassMember('etherWisDeviceRxTestPatternErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                This object counts the number of errors detected when the
                WIS receive path is operating in the PRBS31 test pattern
                mode.  It is reset to zero when the WIS receive path
                initially enters that mode, and it increments each time
                the PRBS pattern checker detects an error as described in
                [IEEE 802.3 Std.] subclause 50.3.8.2 unless its value is
                65535, in which case it remains unchanged.  This object is
                writeable so that it may be reset upon explicit request
                of a command generator application while the WIS receive
                path continues to operate in PRBS31 test pattern mode.
                ''',
                'etherwisdevicerxtestpatternerrors',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisDeviceRxTestPatternMode', REFERENCE_ENUM_CLASS, 'EtherWisDeviceRxTestPatternMode_Enum' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceRxTestPatternMode_Enum', 
                [], [], 
                '''                This variable controls the receive test pattern mode.
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
                ''',
                'etherwisdevicerxtestpatternmode',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisDeviceTxTestPatternMode', REFERENCE_ENUM_CLASS, 'EtherWisDeviceTxTestPatternMode_Enum' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry.EtherWisDeviceTxTestPatternMode_Enum', 
                [], [], 
                '''                This variable controls the transmit test pattern mode.
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
                ''',
                'etherwisdevicetxtestpatternmode',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisDeviceEntry',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisDeviceTable' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisDeviceTable',
            False, 
            [
            _MetaInfoClassMember('etherWisDeviceEntry', REFERENCE_LIST, 'EtherWisDeviceEntry' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry', 
                [], [], 
                '''                An entry in the Ethernet WIS device table.  For each
                instance of this object there MUST be a corresponding
                instance of sonetMediumEntry.
                ''',
                'etherwisdeviceentry',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisDeviceTable',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ETHER-WIS', True),
            _MetaInfoClassMember('etherWisFarEndPathCurrentStatus', REFERENCE_BITS, 'EtherWisFarEndPathCurrentStatus_Bits' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry.EtherWisFarEndPathCurrentStatus_Bits', 
                [], [], 
                '''                This variable indicates the current status at the
                far end of the path using a bit map that can indicate
                multiple defects at once.  The bit positions are
                assigned as follows:
                
                etherWisFarEndPayloadDefect(0)
                   A far end payload defect (i.e., far end
                   PLM-P or LCD-P) is currently being signaled
                   in G1 bits 5-7.
                
                etherWisFarEndServerDefect(1)
                   A far end server defect (i.e., far end
                   LOP-P or AIS-P) is currently being signaled
                   in G1 bits 5-7.  Note:  when this bit is set,
                   sonetPathSTSRDI MUST be set in the corresponding
                   instance of sonetPathCurrentStatus.
                ''',
                'etherwisfarendpathcurrentstatus',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisFarEndPathCurrentEntry',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisFarEndPathCurrentTable' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisFarEndPathCurrentTable',
            False, 
            [
            _MetaInfoClassMember('etherWisFarEndPathCurrentEntry', REFERENCE_LIST, 'EtherWisFarEndPathCurrentEntry' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry', 
                [], [], 
                '''                An entry in the etherWisFarEndPathCurrentTable.  For each
                instance of this object there MUST be a corresponding
                instance of sonetFarEndPathCurrentEntry.
                ''',
                'etherwisfarendpathcurrententry',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisFarEndPathCurrentTable',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ETHER-WIS', True),
            _MetaInfoClassMember('etherWisPathCurrentJ1Received', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                This is the 16-octet path trace message that
                was most recently received in the J1 byte.
                ''',
                'etherwispathcurrentj1received',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisPathCurrentJ1Transmitted', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                This is the 16-octet path trace message that
                is transmitted in the J1 byte.  The value SHOULD
                be '89'h followed by fifteen octets of '00'h
                (or some cyclic shift thereof) when the path
                trace function is not used, and the implementation
                SHOULD use that value (or a cyclic shift thereof)
                as a default if no other value has been set.
                ''',
                'etherwispathcurrentj1transmitted',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisPathCurrentStatus', REFERENCE_BITS, 'EtherWisPathCurrentStatus_Bits' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry.EtherWisPathCurrentStatus_Bits', 
                [], [], 
                '''                This variable indicates the current status of the
                path payload with a bit map that can indicate multiple
                defects at once.  The bit positions are assigned as
                follows:
                
                etherWisPathLOP(0)
                   This bit is set to indicate that an
                   LOP-P (Loss of Pointer - Path) defect
                   is being experienced.  Note:  when this
                   bit is set, sonetPathSTSLOP MUST be set
                   in the corresponding instance of
                   sonetPathCurrentStatus.
                
                etherWisPathAIS(1)
                   This bit is set to indicate that an
                   AIS-P (Alarm Indication Signal - Path)
                   defect is being experienced.  Note:  when
                   this bit is set, sonetPathSTSAIS MUST be
                   set in the corresponding instance of
                   sonetPathCurrentStatus.
                
                etherWisPathPLM(1)
                   This bit is set to indicate that a
                   PLM-P (Payload Label Mismatch - Path)
                   defect is being experienced.  Note:  when
                   this bit is set, sonetPathSignalLabelMismatch
                   MUST be set in the corresponding instance of
                   sonetPathCurrentStatus.
                
                etherWisPathLCD(3)
                   This bit is set to indicate that an
                   LCD-P (Loss of Codegroup Delination - Path)
                   defect is being experienced.  Since this
                   defect is detected by the PCS and not by
                   the path layer itself, there is no
                   corresponding bit in sonetPathCurrentStatus.
                ''',
                'etherwispathcurrentstatus',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisPathCurrentEntry',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisPathCurrentTable' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisPathCurrentTable',
            False, 
            [
            _MetaInfoClassMember('etherWisPathCurrentEntry', REFERENCE_LIST, 'EtherWisPathCurrentEntry' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry', 
                [], [], 
                '''                An entry in the etherWisPathCurrentTable.  For each
                instance of this object there MUST be a corresponding
                instance of sonetPathCurrentEntry.
                ''',
                'etherwispathcurrententry',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisPathCurrentTable',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'ETHER-WIS', True),
            _MetaInfoClassMember('etherWisSectionCurrentJ0Received', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                This is the 16-octet section trace message that
                was most recently received in the J0 byte.
                ''',
                'etherwissectioncurrentj0received',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisSectionCurrentJ0Transmitted', ATTRIBUTE, 'str' , None, None, 
                [(16, None)], [], 
                '''                This is the 16-octet section trace message that
                is transmitted in the J0 byte.  The value SHOULD
                be '89'h followed by fifteen octets of '00'h
                (or some cyclic shift thereof) when the section
                trace function is not used, and the implementation
                SHOULD use that value (or a cyclic shift thereof)
                as a default if no other value has been set.
                ''',
                'etherwissectioncurrentj0transmitted',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisSectionCurrentEntry',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS.EtherWisSectionCurrentTable' : {
        'meta_info' : _MetaInfoClass('ETHERWIS.EtherWisSectionCurrentTable',
            False, 
            [
            _MetaInfoClassMember('etherWisSectionCurrentEntry', REFERENCE_LIST, 'EtherWisSectionCurrentEntry' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry', 
                [], [], 
                '''                An entry in the etherWisSectionCurrentTable.  For each
                instance of this object there MUST be a corresponding
                instance of sonetSectionCurrentEntry.
                ''',
                'etherwissectioncurrententry',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'etherWisSectionCurrentTable',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
    'ETHERWIS' : {
        'meta_info' : _MetaInfoClass('ETHERWIS',
            False, 
            [
            _MetaInfoClassMember('etherWisDeviceTable', REFERENCE_CLASS, 'EtherWisDeviceTable' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisDeviceTable', 
                [], [], 
                '''                The table for Ethernet WIS devices
                ''',
                'etherwisdevicetable',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisFarEndPathCurrentTable', REFERENCE_CLASS, 'EtherWisFarEndPathCurrentTable' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisFarEndPathCurrentTable', 
                [], [], 
                '''                The table for the current far-end state of Ethernet WIS
                paths.
                ''',
                'etherwisfarendpathcurrenttable',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisPathCurrentTable', REFERENCE_CLASS, 'EtherWisPathCurrentTable' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisPathCurrentTable', 
                [], [], 
                '''                The table for the current state of Ethernet WIS paths.
                ''',
                'etherwispathcurrenttable',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisSectionCurrentTable', REFERENCE_CLASS, 'EtherWisSectionCurrentTable' , 'ydk.models.ether.ETHER_WIS', 'ETHERWIS.EtherWisSectionCurrentTable', 
                [], [], 
                '''                The table for the current state of Ethernet WIS sections.
                ''',
                'etherwissectioncurrenttable',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'ETHER-WIS',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.ether.ETHER_WIS'
        ),
    },
}
_meta_table['ETHERWIS.EtherWisDeviceTable.EtherWisDeviceEntry']['meta_info'].parent =_meta_table['ETHERWIS.EtherWisDeviceTable']['meta_info']
_meta_table['ETHERWIS.EtherWisFarEndPathCurrentTable.EtherWisFarEndPathCurrentEntry']['meta_info'].parent =_meta_table['ETHERWIS.EtherWisFarEndPathCurrentTable']['meta_info']
_meta_table['ETHERWIS.EtherWisPathCurrentTable.EtherWisPathCurrentEntry']['meta_info'].parent =_meta_table['ETHERWIS.EtherWisPathCurrentTable']['meta_info']
_meta_table['ETHERWIS.EtherWisSectionCurrentTable.EtherWisSectionCurrentEntry']['meta_info'].parent =_meta_table['ETHERWIS.EtherWisSectionCurrentTable']['meta_info']
_meta_table['ETHERWIS.EtherWisDeviceTable']['meta_info'].parent =_meta_table['ETHERWIS']['meta_info']
_meta_table['ETHERWIS.EtherWisFarEndPathCurrentTable']['meta_info'].parent =_meta_table['ETHERWIS']['meta_info']
_meta_table['ETHERWIS.EtherWisPathCurrentTable']['meta_info'].parent =_meta_table['ETHERWIS']['meta_info']
_meta_table['ETHERWIS.EtherWisSectionCurrentTable']['meta_info'].parent =_meta_table['ETHERWIS']['meta_info']

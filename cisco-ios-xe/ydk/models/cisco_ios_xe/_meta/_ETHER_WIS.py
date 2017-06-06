


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EtherWis.Etherwisdevicetable.Etherwisdeviceentry.EtherwisdevicerxtestpatternmodeEnum' : _MetaInfoEnum('EtherwisdevicerxtestpatternmodeEnum', 'ydk.models.cisco_ios_xe.ETHER_WIS',
        {
            'none':'none',
            'prbs31':'prbs31',
            'mixedFrequency':'mixedFrequency',
        }, 'ETHER-WIS', _yang_ns._namespaces['ETHER-WIS']),
    'EtherWis.Etherwisdevicetable.Etherwisdeviceentry.EtherwisdevicetxtestpatternmodeEnum' : _MetaInfoEnum('EtherwisdevicetxtestpatternmodeEnum', 'ydk.models.cisco_ios_xe.ETHER_WIS',
        {
            'none':'none',
            'squareWave':'squareWave',
            'prbs31':'prbs31',
            'mixedFrequency':'mixedFrequency',
        }, 'ETHER-WIS', _yang_ns._namespaces['ETHER-WIS']),
    'EtherWis.Etherwisdevicetable.Etherwisdeviceentry' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwisdevicetable.Etherwisdeviceentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'ETHER-WIS', True),
            _MetaInfoClassMember('etherWisDeviceRxTestPatternErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
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
            _MetaInfoClassMember('etherWisDeviceRxTestPatternMode', REFERENCE_ENUM_CLASS, 'EtherwisdevicerxtestpatternmodeEnum' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisdevicetable.Etherwisdeviceentry.EtherwisdevicerxtestpatternmodeEnum', 
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
            _MetaInfoClassMember('etherWisDeviceTxTestPatternMode', REFERENCE_ENUM_CLASS, 'EtherwisdevicetxtestpatternmodeEnum' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisdevicetable.Etherwisdeviceentry.EtherwisdevicetxtestpatternmodeEnum', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwisdevicetable' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwisdevicetable',
            False, 
            [
            _MetaInfoClassMember('etherWisDeviceEntry', REFERENCE_LIST, 'Etherwisdeviceentry' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisdevicetable.Etherwisdeviceentry', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwissectioncurrenttable' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwissectioncurrenttable',
            False, 
            [
            _MetaInfoClassMember('etherWisSectionCurrentEntry', REFERENCE_LIST, 'Etherwissectioncurrententry' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
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
            _MetaInfoClassMember('etherWisPathCurrentStatus', REFERENCE_BITS, 'Etherwispathcurrentstatus' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry.Etherwispathcurrentstatus', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwispathcurrenttable' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwispathcurrenttable',
            False, 
            [
            _MetaInfoClassMember('etherWisPathCurrentEntry', REFERENCE_LIST, 'Etherwispathcurrententry' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'ETHER-WIS', True),
            _MetaInfoClassMember('etherWisFarEndPathCurrentStatus', REFERENCE_BITS, 'Etherwisfarendpathcurrentstatus' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry.Etherwisfarendpathcurrentstatus', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis.Etherwisfarendpathcurrenttable' : {
        'meta_info' : _MetaInfoClass('EtherWis.Etherwisfarendpathcurrenttable',
            False, 
            [
            _MetaInfoClassMember('etherWisFarEndPathCurrentEntry', REFERENCE_LIST, 'Etherwisfarendpathcurrententry' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry', 
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
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
    'EtherWis' : {
        'meta_info' : _MetaInfoClass('EtherWis',
            False, 
            [
            _MetaInfoClassMember('etherWisDeviceTable', REFERENCE_CLASS, 'Etherwisdevicetable' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisdevicetable', 
                [], [], 
                '''                The table for Ethernet WIS devices
                ''',
                'etherwisdevicetable',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisFarEndPathCurrentTable', REFERENCE_CLASS, 'Etherwisfarendpathcurrenttable' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwisfarendpathcurrenttable', 
                [], [], 
                '''                The table for the current far-end state of Ethernet WIS
                paths.
                ''',
                'etherwisfarendpathcurrenttable',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisPathCurrentTable', REFERENCE_CLASS, 'Etherwispathcurrenttable' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwispathcurrenttable', 
                [], [], 
                '''                The table for the current state of Ethernet WIS paths.
                ''',
                'etherwispathcurrenttable',
                'ETHER-WIS', False),
            _MetaInfoClassMember('etherWisSectionCurrentTable', REFERENCE_CLASS, 'Etherwissectioncurrenttable' , 'ydk.models.cisco_ios_xe.ETHER_WIS', 'EtherWis.Etherwissectioncurrenttable', 
                [], [], 
                '''                The table for the current state of Ethernet WIS sections.
                ''',
                'etherwissectioncurrenttable',
                'ETHER-WIS', False),
            ],
            'ETHER-WIS',
            'ETHER-WIS',
            _yang_ns._namespaces['ETHER-WIS'],
        'ydk.models.cisco_ios_xe.ETHER_WIS'
        ),
    },
}
_meta_table['EtherWis.Etherwisdevicetable.Etherwisdeviceentry']['meta_info'].parent =_meta_table['EtherWis.Etherwisdevicetable']['meta_info']
_meta_table['EtherWis.Etherwissectioncurrenttable.Etherwissectioncurrententry']['meta_info'].parent =_meta_table['EtherWis.Etherwissectioncurrenttable']['meta_info']
_meta_table['EtherWis.Etherwispathcurrenttable.Etherwispathcurrententry']['meta_info'].parent =_meta_table['EtherWis.Etherwispathcurrenttable']['meta_info']
_meta_table['EtherWis.Etherwisfarendpathcurrenttable.Etherwisfarendpathcurrententry']['meta_info'].parent =_meta_table['EtherWis.Etherwisfarendpathcurrenttable']['meta_info']
_meta_table['EtherWis.Etherwisdevicetable']['meta_info'].parent =_meta_table['EtherWis']['meta_info']
_meta_table['EtherWis.Etherwissectioncurrenttable']['meta_info'].parent =_meta_table['EtherWis']['meta_info']
_meta_table['EtherWis.Etherwispathcurrenttable']['meta_info'].parent =_meta_table['EtherWis']['meta_info']
_meta_table['EtherWis.Etherwisfarendpathcurrenttable']['meta_info'].parent =_meta_table['EtherWis']['meta_info']
